import  mysql.connector
from    mysql.connector import  Error

int_list    =   []
decimal_list    =   []
string_list     =   []

table_name = input("[*] Enter table name : ")

def java_obj():
    filename    =   table_name+".java"
    f = open(filename,"w+")
    f.write("public class %s \n { \n"%(table_name))
    for i in range(len(int_list)):
        f.write("private int    %s ;\n"%(int_list[i]))
    for i in range(len(decimal_list)):
        f.write("private double %s ;\n"%(decimal_list[i]))
    for i in range(len(string_list)):
        f.write("private String %s ;\n"%(string_list[i]))
    for j in range(len(int_list)):
        each = int_list[j]
        f.write("public int f_%s (char p_Type,int p_Value) \n {\n"%(each))
        f.write(" return (p_Type=='G') ? %s :   %s = p_Value ; \n } \n "%(each,each))
    for j in range(len(decimal_list)):
        each = decimal_list[j]
        f.write("public double f_%s (char p_Type,double p_Value) \n { \n"%(each))
        f.write(" return (p_Type=='G') ? %s : %s = p_Value; \n } \n"%(each,each))
    for j in range(len(string_list)):
        each = string_list[j]
        f.write("public String f_%s (char p_Type,String p_Value) \n { \n "%(each))
        f.write(" return (p_Type=='G') ? %s :   %s = p_Value ; \n } \n"%(each,each))
    f.write("\n}\n")
    f.close()


def kotlin_obj():
    filename = table_name+".kt"
    f = open(filename,"w+")
    f.write("class %s \n { \n"%(table_name))
    for i in range(len(int_list)):
        f.write("private var %s : Int = 0 \n"%(int_list[i]))
    for i in range(len(decimal_list)):
        f.write("private var %s : Double = 0.00 \n"%(decimal_list[i]))
    for i in range(len(string_list)):
        f.write("private var %s : String = \"\" \n"%(string_list[i]))
    for j in range(len(int_list)):
        each = int_list[j]
        f.write("fun f_%s (p_Type : Char,p_Value : Int) : Int \n { \n"%(each))
        f.write("   if(p_Type=='G'){ return %s }else{ %s  = p_Value } \n return 0 \n } \n"% (each,each))
    for j in range(len(decimal_list)):
        each = decimal_list[j]
        f.write("fun f_%s (p_Type : Char,p_Value : Double) : Double \n { \n"%(each))
        f.write("   if(p_Type=='G'){ return %s }else{ %s = p_Value } \n return 0.00 \n } \n"% (each,each))
    for j in range(len(string_list)):
        each = string_list[j]
        f.write("fun f_%s (p_Type : Char,p_Value : String) : String \n { \n"% (each))
        f.write("   if(p_Type=='G'){ return %s }else{ %s = p_Value } \n return \"\" \n } \n"% (each,each))
    f.write("\n}")
    f.close()

try:
    connection  =   mysql.connector.connect(host='localhost',database='stlys',user='root',password='jayesh@211')
    sql_query   =   "select column_name ,data_type from information_schema.columns where table_name='%s';" % (table_name)
    cursor  =   connection.cursor()
    cursor.execute(sql_query)
    records =   cursor.fetchall()
    print("==>Total number of rows :",cursor.rowcount)
    print("==>Creating object...")
    for row   in  records:
        row_val = str(row[0])
        each = str(row[1])
        if each=="int":
            int_list.append(row_val)
        elif each=="decimal":
            decimal_list.append(row_val)
        else:
            string_list.append(row_val)
    choice = int(input("[*] Enter '1' for java object or '2' for kotlin object : "))
    if choice == 1:
        java_obj()
    elif choice == 2:
        kotlin_obj()
    else:
        print("***Wrong Input! Please try again***")
        print("==> Closing application...\n BYE")
except:
    print("Error")
finally:
    if(connection.is_connected()):
        connection.close()
        cursor.close()


