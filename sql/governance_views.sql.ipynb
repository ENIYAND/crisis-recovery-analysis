{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "e00ad5ba-4a41-4214-90e4-b17d330c4b1e",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "-- Analysts can read Gold\n",
    "GRANT SELECT ON TABLE food_delivery.gold_daily_kpis TO `analyst_role`;\n",
    "GRANT SELECT ON TABLE food_delivery.gold_customer_risk_profile TO `analyst_role`;\n",
    "\n",
    "-- Data scientists can read Silver\n",
    "GRANT SELECT ON TABLE food_delivery.silver_orders_clean TO `ds_role`;\n",
    "\n",
    "-- Engineers have full access\n",
    "GRANT ALL PRIVILEGES ON SCHEMA food_delivery TO `data_engineer_role`;\n",
    "\n",
    "-- To check privileges:\n",
    "SHOW GRANTS ON SCHEMA food_delivery;\n",
    "SHOW GRANTS ON TABLE food_delivery.gold_daily_kpis;\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "6db737b5-6eab-4243-8826-5d7798e0c4a0",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "* With **Databricks Free Edition**, we cannot create groups.Group creation requires Workspace Admin privileges.\n",
    "\n",
    "* In production, these permissions would be granted to Unity Catalog groups managed by workspace admins. In this project, I just demonstrated the access-control design using logical group names."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "5b93ea1c-6d03-4d9d-84e3-33e304b81330",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "CREATE OR REPLACE VIEW food_delivery.public_orders_safe AS\n",
    "SELECT \n",
    "    s.order_id,\n",
    "    customer_id,\n",
    "    segment,\n",
    "    created_at_simulated,\n",
    "    actual_delivery_time_simulated,\n",
    "    sentiment_category,   -- safe classification\n",
    "    ai_topic              -- safe AI-derived insight\n",
    "FROM food_delivery.silver_orders_enriched s\n",
    "JOIN food_delivery.ai_review_sentiment a ON s.order_id = a.order_id \n",
    ";\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "7b861cb3-8667-4ceb-9481-f09c395bb241",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "I implemented a secure view layer that separates sensitive health-related text from general analytics, enabling privacy-compliant reporting without duplicating data."
   ]
  }
 ],
 "metadata": {
  "application/vnd.databricks.v1+notebook": {
   "computePreferences": null,
   "dashboards": [],
   "environmentMetadata": {
    "base_environment": "",
    "environment_version": "4"
   },
   "inputWidgetPreferences": null,
   "language": "sql",
   "notebookMetadata": {
    "mostRecentlyExecutedCommandWithImplicitDF": {
     "commandId": 6232533490630580,
     "dataframes": [
      "_sqldf"
     ]
    },
    "pythonIndentUnit": 4
   },
   "notebookName": "governance_views.sql",
   "widgets": {}
  },
  "language_info": {
   "name": "sql"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
