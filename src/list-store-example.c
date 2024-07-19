enum {
  COLUMN_STRING,
  COLUMN_INT,
  COLUMN_BOOLEAN,
  N_COLUMNS
};

void refresh ()
{
  GtkListStore *list_store;
  GtkTreePath *path;
  GtkTreeIter iter;
  gint i;

  list_store = gtk_list_store_new (N_COLUMNS,
                                   G_TYPE_STRING,
                                   G_TYPE_INT,
                                   G_TYPE_BOOLEAN);

  for (i = 0; i < 10; i++)
    {
      gchar *some_data;
      some_data = get_some_data (i);

      // Add a new row to the model
      gtk_list_store_append (list_store,
                            &iter);

      gtk_list_store_set (list_store,
                          &iter,
                          COLUMN_STRING,
                          some_data,
                          COLUMN_INT,
                          i,
                          COLUMN_BOOLEAN,
                          FALSE,
                          -1);

      // As the store will keep a copy of the string internally,
      // we free some_data.
      g_free (some_data);
    }

  // Modify a particular row
  path = gtk_tree_path_new_from_string ("4");

  gtk_tree_model_get_iter (GTK_TREE_MODEL (list_store),
                           &iter,
                           path);

  gtk_tree_path_free (path);

  gtk_list_store_set (list_store,
                      &iter,
                      COLUMN_BOOLEAN,
                      TRUE,
                      -1);
}