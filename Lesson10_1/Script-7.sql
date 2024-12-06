SELECT count(*)
from records;

SELECT DATE,aqi,pm25
FROM records
WHERE sitename  = '大城';