# 04_LAB_Q_jihoon

## π μκ΅¬μ¬ν­

- open API 2μ’(μμΈμ νμκ΄ μμ λ°μ΄ν°, μμΈμ κ°μ°λ λ°μ΄ν°)μ νμ©
- GUBN_NAME(νμκ΄ κ΅¬μ²­μλ³ μ½λ) κ³Ό GU_NAME(κ°μ°λ κ΅¬μ²­μλ³ μ½λ) λ±μ νλΌλ©ν°λ‘ μλ ₯λ°μ κ²°ν©λ λ°μ΄ν°λ₯Ό λ¦¬ν΄
- λ°μ΄ν°λ JSONμΌλ‘ μ λ¬
### μμΈμ κ°μ°λ open API μλ΅ sample
http://openapi.seoul.go.kr:8088/sample/json/ListRainfallService/1/2/μ’λ‘κ΅¬  
path variavle : /{index start}/{index end}/{GU_NAME}
~~~
{
    ListRainfallService: {
        list_total_count: 13646,
        RESULT: {
            CODE: "INFO-000",
            MESSAGE: "μ μ μ²λ¦¬λμμ΅λλ€"
            },
        row: [
            {
                RAINGAUGE_CODE: 1002,
                RAINGAUGE_NAME: "λΆμλ",
                GU_CODE: 110,
                GU_NAME: "μ’λ‘κ΅¬",
                RAINFALL10: "0",
                RECEIVE_TIME: "2022-11-18 00:19"
                },
            {
                RAINGAUGE_CODE: 1001,
                RAINGAUGE_NAME: "μ’λ‘κ΅¬μ²­",
                GU_CODE: 110,
                GU_NAME: "μ’λ‘κ΅¬",
                RAINFALL10: "0",
                RECEIVE_TIME: "2022-11-18 00:19"
            }
        ]
    }
}
~~~
### μμΈμ νμκ΄ μμ open API μλ΅ sample
http://openapi.seoul.go.kr:8088/sample/json/DrainpipeMonitoringInfo/1/2/01/2022111700/2022111700  
path variable : /{index start}/{index end}/{GUBN_CODE}/{YYYYMMDDHH}/{YYYYMMDDHH}
~~~
{
    DrainpipeMonitoringInfo: {
        list_total_count: 240,
        RESULT: {
            CODE: "INFO-000",
            MESSAGE: "μ μ μ²λ¦¬λμμ΅λλ€"
            },
        row: [
            {
                IDN: "01-0004",
                GUBN: "01",
                GUBN_NAM: "μ’λ‘",
                MEA_YMD: "2022-11-17 00:00:18.0",
                MEA_WAL: 0.11,
                SIG_STA: "ν΅μ μνΈ",
                REMARK: "μ’λ‘κ΅¬ μΈμ’λλ‘178 λ€ λ§¨ν(KTκ΄νλ¬Έμ¬μ₯λ€ μμ κ±°λ³΄κ΄μμ μ’λ‘1κΈΈ, λ―Έλμ¬κ΄~μ’λ‘μλ°©μ λ¨μΈ‘, μ€νμ² νμ€λ°μ€)"
            },
            {
                IDN: "01-0003",
                GUBN: "01",
                GUBN_NAM: "μ’λ‘",
                MEA_YMD: "2022-11-17 00:00:18.0",
                MEA_WAL: 0.11,
                SIG_STA: "ν΅μ μνΈ",
                REMARK: "μ’λ‘κ΅¬ μνλ¬Έλ‘ 21 μ λ§¨ν(μν΄λΉλ©μμ½λ μΈ‘κ΅¬μΈ‘, λ°±μ΄λμ² νμλ°μ€)"
            }
        ]
    }
}
~~~

## π μ€κ³λ°©ν₯

### μ¬μ© κΈ°μ 
- **Back-End** : Python, Django, Django REST framework, Pandas
- **Database** : SQLite
- **Lint** : Black
- **ETC** : Git, Github

### κ°μ 
1. κ΅¬μ²­λ³ μλ³μ(GUBN_CODE, GU_NAME)λ₯Ό λ΄λ νμ΄λΈ νμ    
2. ν΄λΉ κ΅¬μ²­μ λ°μ΄ν°λ³ κ΄μΈ‘μ μ λ³΄λ₯Ό κ°μ§ νμ΄λΈ νμ    
3. μμ²­μ 1λ²μ ν΄λΉνλ DBμ κ΅¬μ²­νμ΄λΈμ κ° κ΅¬μ²­λ³ idλ₯Ό ν΅ν΄μ path variableλ‘ μ‘°ν (ex. /some_domain/seoul/\<int:gu_id\>/)
4. 1,2λ²μ ν΄λΉνλ λ΄μ©μ batch μ±μ λ°λ‘ μμ±ν΄ django-admin custom commandλ‘ csv dataλ₯Ό ν΄λΉ νμ΄λΈμ μ½μ  

### ERD
<img src="./img/LAB_Q_erd.png" width="600">

### API Endpoint
|INDEX|URI|METHOD|DESC|
|:---:|:---|:---:|:---:|
|1|/seoul/|GET|μμΈμ κ΅¬μ²­λ¦¬μ€νΈ μ‘°ν|
|2|/seoul/\<int:gu_id\>/|GET|κ΅¬μ²­λ³ μμ²­ λ°μ΄ν° μ‘°ν|
