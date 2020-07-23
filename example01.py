import pymysql

def main():
    no = int(input('要编辑的部门标号：'))
    loc = input('部门的新地址：')
    # 1. 创建连接对象
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', db='hrs', charset='utf8')
    print(conn)
     # 打开游标上下文，with 离开时会自动关，没有with 需要手动关
    try:
        # 2.获得游标对象
        with conn.cursor() as cursor:
            # 3.执行SQL语句得到结果
            # result = cursor.execute('insert into tb_dept values (90, "销售二部", "重庆")')
            # result = cursor.execute('delete from tb_dept where dno=%s', (no,))
            result = cursor.execute('update tb_dept set dloc=%s where dno=%s', (loc, no))
        # 成功需要手动提交
            if result == 1:\
                print('添加成功')
            # 4. 操作成功执行提交
            conn.commit()
    except pymysql.MySQLError as error:
        print(error)
        # 4. 操作失败执行回滚
        conn.rollback()
    finally:
        # 5. 关闭连接释放资源
        conn.close()





if __name__ == '__main__':
    main()