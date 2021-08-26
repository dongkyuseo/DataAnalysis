
import pymysql

def get_monthly(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = """
        SELECT DATE_FORMAT(sdate, '%m') AS `month`, 
            SUM(revenue) AS revenue, SUM(profit) AS profit
            FROM sales_list
            GROUP BY `month`
            ORDER BY `month`;
    """
    cur.execute(sql)
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results


def get_company_rp(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = """
        SELECT scompany AS `company`, 
            sum(revenue) AS `rev`, SUM(profit) AS `pro`
            FROM sales_list
            GROUP BY `company`
            ORDER BY `company`;
    """
    cur.execute(sql)
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results


def get_company_nu(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = """
        SELECT scompany AS `company`, 
            pname AS `name`, SUM(sunit) AS `unit`
            FROM sales_list
            GROUP BY `company`, `name`
            ORDER BY `company`;
    """
    cur.execute(sql)
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results


def get_pname_rp(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = """
        SELECT pname AS `name`, 
            sum(sunit) as `unit`, sum(revenue) AS `rev`, SUM(profit) AS `pro`
            FROM sales_list
            GROUP BY `name`
            ORDER BY `name`;
    """
    cur.execute(sql)
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results


def get_category_rp(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = """
        SELECT pcategory AS `category`, 
            sum(revenue) AS `rev`, SUM(profit) AS `pro`
            FROM sales_list
            GROUP BY `category`
            ORDER BY `category`;
    """
    cur.execute(sql)
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results