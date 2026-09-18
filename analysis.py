import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/support_tickets.csv")
print("Shape:", df.shape)
print("Missing values:\n", df.isna().sum())
print("Duplicate ticket IDs:", df["ticket_id"].duplicated().sum())

df["ticket_date"] = pd.to_datetime(df["ticket_date"])
df["category"] = df["category"].str.strip()
df["priority"] = df["priority"].str.strip()

kpis = pd.Series({
    "total_tickets": len(df),
    "resolved_tickets": int((df["status"]=="Resolved").sum()),
    "avg_resolution_hours": round(df["resolution_hours"].mean(),2),
    "sla_compliance_pct": round((df["sla_status"]=="Met").mean()*100,2),
    "avg_customer_satisfaction": round(df["customer_satisfaction"].mean(),2)
})
print("\nKPIs:\n", kpis)

summary=df.groupby("category").agg(
    tickets=("ticket_id","count"),
    avg_resolution_hours=("resolution_hours","mean"),
    avg_satisfaction=("customer_satisfaction","mean")
).sort_values("tickets",ascending=False)

summary.round(2).to_csv("../outputs/category_summary.csv")
df.to_csv("../outputs/cleaned_support_tickets.csv",index=False)
summary["tickets"].plot(kind="bar",title="Ticket Volume by Category")
plt.tight_layout()
plt.savefig("../outputs/ticket_volume_by_category.png",dpi=160)
