from fastmcp import FastMCP
import sqlite3

# Create an MCP server
mcp = FastMCP("Todos Server")

DB_PATH = r"c:\classroom\mar4\todos\todos.db"

# Add todo
@mcp.tool()
def add_todo(todo: str, importance : str ='normal') -> bool:
    """Adds a new Todo"""
    print(f'Add is called with {todo} and {importance}')
    try:
        # connect to db
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("insert into todos (todo, importance) values(?,?)",
                       (todo, importance))
        conn.commit()
        conn.close()
        return True
    except Exception as ex:
        print(ex)
        return False


@mcp.tool()
def update_importance(todo: str, importance : str ='normal') -> bool:
    """Updates importance of all todos that contain the given todo string"""
    print(f'update_todo is called with {todo} and {importance}')
    try:
        # connect to db
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("update  todos set importance = ? where completedon is null  and todo like ?",
                       (importance, f'%{todo}%'))
        conn.commit()
        conn.close()
        return True
    except Exception as ex:
        print(ex)
        return False


@mcp.tool()
def get_todos_by_importance(importance : str ='normal') -> list[dict] | None:
    """Retrieve all todos based on the given importance"""
    print(f'todos_by_importance is called with importance = {importance}')
    try:
        # connect to db
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("select todo, addedon from todos where completedon is null and importance = ?",
                       (importance.lower(),))
        todos = []
        for row in cursor.fetchall():
            todos.append({"todo": row[0], "addedon": row[1]})

        conn.close()
        return todos
    except Exception as ex:
        print(ex)
        return None


@mcp.tool()
def get_recent_todos(count: int = 5) -> list[dict] | None:
    """Retrieve count number of recently added todos"""
    print(f'recent_todos is called with count = {count}')
    try:
        # connect to db
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("select todo, addedon, importance from todos where completedon is null order by addedon desc limit ?",
                       (count,))
        todos = []
        for row in cursor.fetchall():
            todos.append({"todo": row[0],
                          "addedon": row[1],
                          "importance": row[2]})

        conn.close()
        return todos
    except Exception as ex:
        print(ex)
        return None


@mcp.tool()
def get_all_todos() -> list[dict] | None:
    """Retrieve all todos"""
    print('get_all_todos is called')
    try:
        # connect to db
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            "select todo, addedon, importance from todos where completedon is null")
        todos = []
        for row in cursor.fetchall():
            todos.append({"todo": row[0],
                          "addedon": row[1],
                          "importance": row[2]})

        conn.close()
        return todos
    except Exception as ex:
        print(ex)
        return None


# Delete todo
@mcp.tool()
def delete_todos(todo: str) -> int | None:
    """Deletes all todos where given string is present in todo and returns the number of todos deleted"""
    print(f'delete is called with todo = {todo}')
    try:
        # connect to db
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("delete from todos where todo like ? and completedon is null", (f'%{todo}%',))
        count = cursor.rowcount
        conn.commit()
        conn.close()
        return count
    except Exception as ex:
        print(ex)
        return None


@mcp.tool()
def complete_todo(todo: str) -> bool:
    """Updates COMPLETEDON of all todos that contains the given todo string"""
    print(f'complete_todo is called with {todo}')
    try:
        # connect to db
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("update  todos set completedon = DATE('now') where todo like ?",
                    (f'%{todo}%',))
        conn.commit()
        conn.close()
        return True
    except Exception as ex:
        print(ex)
        return False

@mcp.tool()
def get_completed_todos() -> list[dict] | None:
    """Retrieve all todos that were completed"""
    
    print('get_completed_todos is called')
    try:
        # connect to db
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("select todo, addedon, importance, completedon from todos where completedon is not null")
        todos = []
        for row in cursor.fetchall():
            todos.append(
                         {"todo": row[0],
                          "addedon": row[1],
                          "importance": row[2],
                          "completedon": row[3]}
                        )

        conn.close()
        return todos
    except Exception as ex:
        print(ex)
        return None
    

 

if __name__ == '__main__':
    mcp.run(transport="http", port=9999)
