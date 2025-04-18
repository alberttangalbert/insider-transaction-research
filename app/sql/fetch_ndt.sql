SELECT 
    ndt.ACCESSION_NUMBER, 
    ndt.TRANS_DATE,
    ndt.TRANS_CODE, 
    ndt.EQUITY_SWAP_INVOLVED, 
    ndt.TRANS_SHARES, 
    ndt.TRANS_PRICEPERSHARE, 
    ndt.TRANS_ACQUIRED_DISP_CD,
    ndh.SHRS_OWND_FOLWNG_TRANS,
    ndt.DIRECT_INDIRECT_OWNERSHIP,
    cm.COMPANY_ID,
    ro.RPTOWNERNAME,
    ro.RPTOWNER_RELATIONSHIP,
    ro.RPTOWNER_TITLE
FROM VERDAD.INSIDER_TRADING.NONDERIV_TRANS AS ndt
JOIN VERDAD.INSIDER_TRADING.NONDERIV_HOLDING AS ndh 
    ON ndt.ACCESSION_NUMBER = ndh.ACCESSION_NUMBER
JOIN VERDAD.INSIDER_TRADING.SUBMISSION AS sub 
    ON ndt.ACCESSION_NUMBER = sub.ACCESSION_NUMBER
JOIN VERDAD.INSIDER_TRADING.CIK_MAPPING AS cm 
    ON sub.ISSUERCIK = cm.CIK_ID
JOIN VERDAD.INSIDER_TRADING.REPORTINGOWNER AS ro 
    ON ndt.ACCESSION_NUMBER = ro.ACCESSION_NUMBER
ORDER BY ndt.accession_number, ndt.TRANS_DATE