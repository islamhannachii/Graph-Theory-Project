from flask import Flask, json, request, jsonify, url_for, render_template,session
from werkzeug.utils import redirect
from bellmanFord import Graphee
from djkstra import Graphe
from connexe.Graph import Graph
import networkx as nx 
import matplotlib.pyplot as plt
from ast import literal_eval
import math
from markupsafe import escape
from flask_session import Session
from datetime import timedelta
#################################################################################
app = Flask(__name__)
#################################################################################
app.secret_key = "hello"
app.permanent_seesion_lifetime = timedelta(minutes=20)
#################################################################################
############################################################################
############################################################################

############################################################################
#djkstra
############################################################################
@app.route('/algo1/<mat>&<int:racine>')
def algo1(mat,racine):
    if(mat and racine):
        mat = json.loads(mat)
        k = Graphe(mat)
        y = k.dijkstra(int(racine))
        o = k.ordre_cal()
        row =[]
        a_list = []
        for i in range(len(o)):
            row.append(o[i][0])
            row.append(o[i][1])
            a_list.append(tuple(row))
            row =[]
        return render_template('djkstra.html',mat = mat, matrice = y, ordre = o, len1 = len(mat),len2=len(o),len3 = len(y), newlist=a_list)

##############################################################################
#bellmanFord
##############################################################################
@app.route('/algo2<mat>&<int:racine>')
def algo2(mat,racine):
    if(mat and racine):
        mat = json.loads(mat)
        k = Graphee(mat)
        y = k.bellmanFord(racine)
        o = k.ordre_cal()
        row =[]
        a_list = []
        for i in range(len(o)):
            row.append(o[i][0])
            row.append(o[i][1])
            a_list.append(tuple(row))
            row =[]
        
        return render_template('bellmanFord.html',mat = mat, matrice = y, ordre = o, len1 = len(mat),len2=len(o),len3 = len(y),newlist=a_list)
##############################################################################
#La  matrice
##############################################################################
@app.route("/matrice/<int:len>/",methods=["Get","Post"])
def matrice(len):
    if (request.method == "GET"):
        return render_template('matrice.html',len=len)
    else:
        if(request.method == "POST"):
            session.permanent = True
            M =[]
            i = 0
            while (i < int(len)):
                j = 0
                row=[]
                while (j< int(len)):
                    data = int(request.form[str(i)+str(j)])
                    row.append(data)
                    j+=1
                M.append(row)
                i+=1
            racine = int(request.form['racine'])
 
            x = int(len)
            g = Graph(x)
            for i in range(len):
                for j in range(len):
                    if(M[i][j]):
                        g.addEdge(i, j)
            x = g.connectedComponents()
            if x== True:            
                if (request.form['algo'] == "2"):
                    return redirect(url_for('algo2',mat =M, racine = int(racine)))
                else:
                    for i in range(len):
                        for j in range(len):
                            if M[i][j] and i==j:
                                session['error'] = "Le graphe admet de boucles, s'il vous plait verifiez votre matrice !!"
                                return redirect(url_for('matrice',len=len))
                            if M[i][j] <0:
                                session['error'] = "Le graphe a de poids negatif, s'il vous plait verifiez votre matrice !!"
                                return redirect(url_for('matrice',len=len))
                    return redirect(url_for('algo1',mat =M, racine = int(racine)))
            else :
                session['error'] = "Le graphe doit etre connexe"
                return redirect(url_for('matrice',len=len))
            
        
            
##############################################################################
#Home page
##############################################################################

@app.route("/taille/",methods=["GET","POST"])
def taille():
    if (request.method == "POST"):
        if (request.form['len']):
            return redirect(url_for('matrice',len=int(request.form['len'])))
        else:
            render_template('taille.html')
    if (request.method == "GET"):
        return render_template('taille.html',title="Remplir le matrice")

######################################################################
#Le Dessin
######################################################################
@app.route('/dessin/<ordre>&<nbrsommets>')
def dessin(ordre,nbrsommets):
    if (ordre):
        ordre = literal_eval(ordre)
        G = nx.DiGraph()
        G.add_node(int(nbrsommets))
        for i in ordre:
            if ((i[0],i[1])):
                G.add_edge(i[0],i[1],weight=i[2])
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=250,node_color="blue",edge_color="red")
        nx.draw_networkx_edge_labels(G, pos, font_size=9, edge_labels=nx.get_edge_attributes(G,'weight'))
        plt.show()
        return "<h3>Le graphe sera afficher</h3>"
@app.route('/')
def home():
    return redirect(url_for('taille'))


if __name__ == "__main__":
    sess = Session()
    sess.init_app(app)
    app.run(debug=True)
