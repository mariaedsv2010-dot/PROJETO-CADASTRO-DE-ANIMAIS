import sqlite3 # banco de dados
import tkinter as tk # lib de interface gráfica
from tkinter import messagebox, ttk # caixa de msg / tkinter


def conectar():
    return sqlite3.connect('teste.db')

# CREATE READ UPDATE DELETE

# banco de dados
def criar_tabela():
    conn = conectar()
    c = conn.cursor() # digitar sql num arquivo python
    c.execute('''
               CREATE TABLE IF NOT EXISTS usuarios(
             
              id INTEGER NOT NULL,
              nome TEXT NOT NULL,
              raca TEXT NOT NULL,
              peso REAL NOT NULL,
              altura REAL NOT NULL,
              vacina TEXt NOT NULL
             
              )''')
    conn.commit()
    conn.close()          



# CREATE CRUD

def inserir_usuario():
    cpf   =  entry_cpf.get().strip()
    nome  =  entry_nome.get().strip()
    raca =  entry_raca.get().strip()
    peso = float(entry_peso.get())
    altura =float(entry_altura.get())
    vacina = entry_vacina.get().strip()
   
    if cpf and nome and raca and peso and altura and vacina:
    #    try:
            conn  =  conectar()
            c = conn.cursor()
            c.execute('INSERT INTO usuarios (id, nome,raca,peso,altura,vacina ) VALUES (?,?,?,?,?,?)', (cpf, nome, raca, peso, altura,vacina))
            conn.commit()
            conn.close()
            messagebox.showinfo('Dados','DADOS INSERIDOS COM SUCESSO!')
            mostra_usuario()
            entry_cpf.delete(0, tk.END)
            entry_nome.delete(0, tk.END)
            entry_raca.delete(0, tk.END)
            entry_peso.delete(0, tk.END)
            entry_altura.delete(0, tk.END)
            entry_vacina.delete(0, tk.END)
    #    except sqlite3.IntegrityError:
    #         messagebox.showerror('Erro', 'O DADO JA EXISTE')

    else:
        messagebox.showwarning('Dado', 'INSIRA TODOS OS DADOS')


def mostra_usuario():
    for row in tree.get_children():
        tree.delete(row)
    conn  =  conectar()
    c = conn.cursor()        
    c.execute('SELECT * FROM usuarios')
    usuarios =  c.fetchall()
    for usuario in usuarios:
        tree.insert('', 'end', values=usuario)
    conn.close()    


# ATUALIZAR
def editar(): 
    selecao = tree.selection()
    user_id  =  tree.item(selecao)['values'][0]
    if selecao:
       
        novo_nome  =  entry_nome.get()
        novo_raça =  entry_raca.get()
        novo_peso = entry_peso.get()
        novo_altura = entry_peso.get()
        novo_vacina = entry_vacina.get()
        if  novo_nome and novo_raça and novo_peso and novo_altura and novo_vacina:
            try:
                conn  =  conectar()
                c = conn.cursor()
                c.execute('UPDATE usuarios SET nome = ?,  raça = ? , peso = ?, altura = ?, vacina = ?,WHERE id = ?' (novo_nome, novo_raça,novo_peso,novo_altura,novo_vacina, user_id))
                conn.commit()
                conn.close()
                messagebox.showinfo('Dados','DADOS INSERIDOS COM SUCESSO!')
                mostra_usuario()
                entry_cpf.delete(0, tk.END)
                entry_nome.delete(0, tk.END)
                entry_raca.delete(0, tk.END)
                entry_peso.delete(0 , tk.END)
                entry_altura.delete(0, tk.END)
                entry_vacina.delete(0, tk.END)
            except:
                messagebox.showerror('Erro', 'OCORREU UM ERRO AO INSERIR OS DADOS, VERIFIQUE')
    else:
        messagebox.showwarning('Dado', 'INSIRA TODOS OS DADOS')





# DELETAR

def deletar_usuario():
    selecao = tree.selection()
    if selecao:
        user_id  =  tree.item(selecao)['values'][0]
        conn  =  conectar()
        c = conn.cursor()
        c.execute('DELETE FROM usuarios WHERE id = ?', (user_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo('Dados', 'DADOS DELETADOS COM SUCESSO!')
        mostra_usuario()
    else:
        messagebox.showerror('Dados', 'ERRO AO DELEETAR OS DADOS!')    
     
   


# interface grafica
janela = tk.Tk()
janela.geometry('650x500')
janela.title('...CRUD...')

style = ttk.Style()
style.theme_use('clam')
style.configure('TLabel', background = 'white', font = ('arial', 10))
style.configure('TEntry', font = ('Segoe UI', 10))
style.configure('TButton', font = ('Segoe UI', 10), padding = 6)
style.configure('Treeview.Hending', font = ('Segoe UI', 10, 'bold'))
style.configure('Treeview',font = ('Segoe UI', 10, 'bold'))


# frames  -  sessão
main_frame =  ttk.Frame(janela, padding=15)
main_frame.pack(fill=tk.BOTH, expand=True)


# widgets -  elementos  

titulo = ttk.Label(main_frame, text=' Cadastro de animais', font=('Segoe UI', 10, 'bold'))
titulo.grid(row=0, columnspan=2,pady=(0,15), sticky='w')
###############################

input_frame =  ttk.LabelFrame(main_frame, text='DADOS DO USUARIO', padding=10)
input_frame.grid(row=1,column= 0, columnspan = 2, sticky='ew', pady=(0,15))

# textos para direcionar
# CPF
ttk.Label(input_frame, text='ID').grid(row=0, column=0, padx=(0,10), pady=5, sticky='e')

entry_cpf = ttk.Entry(input_frame, width=30)
entry_cpf.grid(row=0, column=1, padx=(0,20), pady=5, sticky='w')

# textos para direcionar
# NOME
ttk.Label(input_frame, text='NOME').grid(row=1, column=0, padx=(0,10), pady=5, sticky='e')

entry_nome = ttk.Entry(input_frame, width=30)
entry_nome.grid(row=1, column=1, padx=(0,20), pady=5, sticky='w')


# textos para direcionar
# RAÇA
ttk.Label(input_frame, text='RAÇA').grid(row=2, column=0, padx=(0,10), pady=5, sticky='e')

entry_raca = ttk.Entry(input_frame, width=30)
entry_raca.grid(row=2, column=1, padx=(0,20), pady=5, sticky='w')

# PESO
ttk.Label(input_frame, text='PESO').grid(row= 3, column=0, padx= (0,10), pady=5, sticky= 'e')


entry_peso = ttk.Entry(input_frame,width=30 )
entry_peso.grid(row= 3,column=1,padx=(0,20), pady=5, sticky= 'w')

#ALTURA

ttk.Label(input_frame, text= 'ALTURA').grid(row = 4, column=0, padx=(0,10),pady=5, sticky='e')

entry_altura= ttk.Entry(input_frame,width=30)
entry_altura.grid(row = 4,column=1,padx=(0,20),pady= 5, sticky= 'w')

ttk.Label(input_frame, text= 'VACINA').grid(row = 5, column=0, padx=(0,10),pady=5, sticky='e')

entry_vacina= ttk.Entry(input_frame,width=30)
entry_vacina.grid(row = 5,column=1,padx=(0,20),pady= 5, sticky= 'w')

# botões
btn_frame = ttk.Frame(main_frame)
btn_frame.grid(row=2, column=0, columnspan=2, pady=(0,15), sticky='ew')


btn_salvar = ttk.Button(btn_frame, text='SALVAR', command=inserir_usuario)
btn_salvar.pack(side = tk.LEFT, padx=5 )

btn_atualizar = ttk.Button(btn_frame, text='ATUALIZAR')
btn_atualizar.pack(side = tk.LEFT, padx=5 )

btn_deletar = ttk.Button(btn_frame, text='DELETAR', command= deletar_usuario)
btn_deletar.pack(side = tk.LEFT, padx=5 )

# btn_limpar = ttk.Button(btn_frame, text='LIMPAR')
# btn_limpar.pack(side = tk.LEFT, padx=5 )

# Treeview - vizualizar os dados

tree_frame = ttk.Frame(main_frame)
tree_frame.grid(row=3, column=0, columnspan=2, sticky='nsew')

main_frame.columnconfigure(0, weight = 1)
main_frame.rowconfigure(3,weight = 1)

# criação da TreeView
columns = ('ID', 'NOME', 'RAÇA','PESO','ALTURA','VACINA')
tree = ttk.Treeview(tree_frame, columns=columns, show='headings', height=12)
tree.pack(fill=tk.BOTH, expand=True)

for col in columns:
    tree.heading(col, text= col)
    tree.column(col, width=180, anchor='center')

# scrolbar -  barra rolagem

scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

criar_tabela()
mostra_usuario()

janela.mainloop()