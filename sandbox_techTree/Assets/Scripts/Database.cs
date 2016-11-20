using System.Collections;
using Mono.Data.Sqlite;
using System.Data;
using System;
using System.Collections.Generic;
using Gurkenhobel.TechTree;
using UnityEngine;

public class Database : MonoBehaviour, IDisposable
{
    string _conn; 
    IDbConnection _dbconn;

    void Awake()
    {
        _conn = "URI=file:" + Application.dataPath + "/Database/techTree.s3db";
        _dbconn = (IDbConnection)new SqliteConnection(_conn);
        _dbconn.Open(); 
    }

    public List<IUpgrade> GetChildren(int parentId)
    {
        var result = new List<IUpgrade>();

        IDbCommand dbcmd = _dbconn.CreateCommand();
        string sqlQuery = "SELECT name FROM techtree WHERE parent = " + parentId;
        dbcmd.CommandText = sqlQuery;
        IDataReader reader = dbcmd.ExecuteReader();
        while (reader.Read())
        {
            print(reader.GetString(0));
        }

        return result;
    }

    public void Dispose()
    {
        _dbconn.Close();
        _dbconn = null;
    }
}
