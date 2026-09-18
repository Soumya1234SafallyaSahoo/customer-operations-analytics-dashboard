-- Customer Operations Analytics KPI Queries

SELECT COUNT(*) AS total_tickets FROM support_tickets;

SELECT ROUND(AVG(resolution_hours),2) AS avg_resolution_hours
FROM support_tickets;

SELECT ROUND(100.0 * SUM(CASE WHEN sla_status='Met' THEN 1 ELSE 0 END)
       / COUNT(*),2) AS sla_compliance_pct
FROM support_tickets;

SELECT category, COUNT(*) AS ticket_count,
       ROUND(AVG(resolution_hours),2) AS avg_resolution_hours,
       ROUND(AVG(customer_satisfaction),2) AS avg_satisfaction
FROM support_tickets
GROUP BY category
ORDER BY ticket_count DESC;

SELECT priority, COUNT(*) AS ticket_count,
       ROUND(100.0 * SUM(CASE WHEN sla_status='Met' THEN 1 ELSE 0 END)
       / COUNT(*),2) AS sla_compliance_pct
FROM support_tickets
GROUP BY priority;
