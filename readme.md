SAP - Order-to-Cash (O2C) automation with Agent Development Kit (ADK)
==============================================================

# MCP servers and tools


## OpenAPI specification to MCP Server
Using the `openapi-mcp-generator` tool we can generate MCP servers based on OpenAPI specifications. 
example command:
```
openapi-mcp-generator \
  --input ./sap_api/API_SALES_ORDER_SRV.json \
  --output ./generated/API_SALES_ORDER_SRV \
  --server-name API_SALES_ORDER_SRV \
  --base-url http://256.256.256.11:50000/sap/opu/odata/sap/API_SALES_ORDER_SRV/
```

## API_SALES_ORDER_SRV server
```
GetASalesorder
PostASalesorder
GetASalesorder___salesorder___
DeleteASalesorder___salesorder___
PatchASalesorder___salesorder___
GetASalesorder___salesorder___ToBillingplan
GetASalesorder___salesorder___ToItem
PostASalesorder___salesorder___ToItem
GetASalesorder___salesorder___ToPartner
PostASalesorder___salesorder___ToPartner
GetASalesorder___salesorder___ToPaymentplanitemdetails
PostASalesorder___salesorder___ToPaymentplanitemdetails
GetASalesorder___salesorder___ToPrecedingprocflowdoc
GetASalesorder___salesorder___ToPricingelement
PostASalesorder___salesorder___ToPricingelement
GetASalesorder___salesorder___ToRelatedobject
PostASalesorder___salesorder___ToRelatedobject
GetASalesorder___salesorder___ToSubsequentprocflowdoc
GetASalesorder___salesorder___ToText
PostASalesorder___salesorder___ToText
GetASalesorderbillingplan
GetASalesorderbillingplan_salesorder___salesorder___billingplan___billingplan___
PatchASalesorderbillingplan_salesorder___salesorder___billingplan___billingplan___
GetASalesorderbillingplan_salesorder___salesorder___billingplan___billingplan___ToBillingplanitem
PostASalesorderbillingplan_salesorder___salesorder___billingplan___billingplan___ToBillingplanitem
GetASalesorderbillingplan_salesorder___salesorder___billingplan___billingplan___ToSalesorder
GetASalesorderbillingplanitem
PostASalesorderbillingplanitem
GetASalesorderbillingplanitem_salesorder___salesorder___billingplan___billingplan___billingplanitem___billingplanitem___
DeleteASalesorderbillingplanitem_salesorder___salesorder___billingplan___billingplan___billingplanitem___billingplanitem___
PatchASalesorderbillingplanitem_salesorder___salesorder___billingplan___billingplan___billingplanitem___billingplanitem___
GetASalesorderbillingplanitem_salesorder___salesorder___billingplan___billingplan___billingplanitem___billingplanitem___ToBillingplan
GetASalesorderbillingplanitem_salesorder___salesorder___billingplan___billingplan___billingplanitem___billingplanitem___ToSalesorder
GetASalesorderheaderpartner
PostASalesorderheaderpartner
GetASalesorderheaderpartner_salesorder___salesorder___partnerfunction___partnerfunction___
DeleteASalesorderheaderpartner_salesorder___salesorder___partnerfunction___partnerfunction___
PatchASalesorderheaderpartner_salesorder___salesorder___partnerfunction___partnerfunction___
GetASalesorderheaderpartner_salesorder___salesorder___partnerfunction___partnerfunction___ToAddress
GetASalesorderheaderpartner_salesorder___salesorder___partnerfunction___partnerfunction___ToSalesorder
GetASalesorderheaderprelement
PostASalesorderheaderprelement
GetASalesorderheaderprelement_salesorder___salesorder___pricingprocedurestep___pricingprocedurestep___pricingprocedurecounter___pricingprocedurecounter___
DeleteASalesorderheaderprelement_salesorder___salesorder___pricingprocedurestep___pricingprocedurestep___pricingprocedurecounter___pricingprocedurecounter___
PatchASalesorderheaderprelement_salesorder___salesorder___pricingprocedurestep___pricingprocedurestep___pricingprocedurecounter___pricingprocedurecounter___
GetASalesorderheaderprelement_salesorder___salesorder___pricingprocedurestep___pricingprocedurestep___pricingprocedurecounter___pricingprocedurecounter___ToSalesorder
GetASalesorderitem
PostASalesorderitem
GetASalesorderitem_salesorder___salesorder___salesorderitem___salesorderitem___
DeleteASalesorderitem_salesorder___salesorder___salesorderitem___salesorderitem___
PatchASalesorderitem_salesorder___salesorder___salesorderitem___salesorderitem___
GetASalesorderitem_salesorder___salesorder___salesorderitem___salesorderitem___ToBillingplan
GetASalesorderitem_salesorder___salesorder___salesorderitem___salesorderitem___ToPartner
PostASalesorderitem_salesorder___salesorder___salesorderitem___salesorderitem___ToPartner
GetASalesorderitem_salesorder___salesorder___salesorderitem___salesorderitem___ToPrecedingprocflowdocitem
GetASalesorderitem_salesorder___salesorder___salesorderitem___salesorderitem___ToPricingelement
PostASalesorderitem_salesorder___salesorder___salesorderitem___salesorderitem___ToPricingelement
GetASalesorderitem_salesorder___salesorder___salesorderitem___salesorderitem___ToRelatedobject
PostASalesorderitem_salesorder___salesorder___salesorderitem___salesorderitem___ToRelatedobject
GetASalesorderitem_salesorder___salesorder___salesorderitem___salesorderitem___ToSalesorder
GetASalesorderitem_salesorder___salesorder___salesorderitem___salesorderitem___ToScheduleline
PostASalesorderitem_salesorder___salesorder___salesorderitem___salesorderitem___ToScheduleline
GetASalesorderitem_salesorder___salesorder___salesorderitem___salesorderitem___ToSubsequentprocflowdocitem
GetASalesorderitem_salesorder___salesorder___salesorderitem___salesorderitem___ToText
PostASalesorderitem_salesorder___salesorder___salesorderitem___salesorderitem___ToText
GetASalesorderitembillingplan
GetASalesorderitembillingplan_salesorder___salesorder___salesorderitem___salesorderitem___billingplan___billingplan___
PatchASalesorderitembillingplan_salesorder___salesorder___salesorderitem___salesorderitem___billingplan___billingplan___
GetASalesorderitembillingplan_salesorder___salesorder___salesorderitem___salesorderitem___billingplan___billingplan___ToBillingplanitem
PostASalesorderitembillingplan_salesorder___salesorder___salesorderitem___salesorderitem___billingplan___billingplan___ToBillingplanitem
GetASalesorderitembillingplan_salesorder___salesorder___salesorderitem___salesorderitem___billingplan___billingplan___ToSalesorder
GetASalesorderitembillingplan_salesorder___salesorder___salesorderitem___salesorderitem___billingplan___billingplan___ToSalesorderitem
GetASalesorderitempartner
PostASalesorderitempartner
GetASalesorderitempartner_salesorder___salesorder___salesorderitem___salesorderitem___partnerfunction___partnerfunction___
DeleteASalesorderitempartner_salesorder___salesorder___salesorderitem___salesorderitem___partnerfunction___partnerfunction___
PatchASalesorderitempartner_salesorder___salesorder___salesorderitem___salesorderitem___partnerfunction___partnerfunction___
GetASalesorderitempartner_salesorder___salesorder___salesorderitem___salesorderitem___partnerfunction___partnerfunction___ToAddress
GetASalesorderitempartner_salesorder___salesorder___salesorderitem___salesorderitem___partnerfunction___partnerfunction___ToSalesorder
GetASalesorderitempartner_salesorder___salesorder___salesorderitem___salesorderitem___partnerfunction___partnerfunction___ToSalesorderitem
GetASalesorderitempartneraddress
GetASalesorderitempartneraddress_salesorder___salesorder___salesorderitem___salesorderitem___partnerfunction___partnerfunction___addressrepresentationcode___addressrepresentationcode___
PatchASalesorderitempartneraddress_salesorder___salesorder___salesorderitem___salesorderitem___partnerfunction___partnerfunction___addressrepresentationcode___addressrepresentationcode___
GetASalesorderitempartneraddress_salesorder___salesorder___salesorderitem___salesorderitem___partnerfunction___partnerfunction___addressrepresentationcode___addressrepresentationcode___ToPartner
GetASalesorderitempartneraddress_salesorder___salesorder___salesorderitem___salesorderitem___partnerfunction___partnerfunction___addressrepresentationcode___addressrepresentationcode___ToSalesorder
GetASalesorderitempartneraddress_salesorder___salesorder___salesorderitem___salesorderitem___partnerfunction___partnerfunction___addressrepresentationcode___addressrepresentationcode___ToSalesorderitem
GetASalesorderitemprelement
PostASalesorderitemprelement
GetASalesorderitemprelement_salesorder___salesorder___salesorderitem___salesorderitem___pricingprocedurestep___pricingprocedurestep___pricingprocedurecounter___pricingprocedurecounter___
DeleteASalesorderitemprelement_salesorder___salesorder___salesorderitem___salesorderitem___pricingprocedurestep___pricingprocedurestep___pricingprocedurecounter___pricingprocedurecounter___
PatchASalesorderitemprelement_salesorder___salesorder___salesorderitem___salesorderitem___pricingprocedurestep___pricingprocedurestep___pricingprocedurecounter___pricingprocedurecounter___
GetASalesorderitemprelement_salesorder___salesorder___salesorderitem___salesorderitem___pricingprocedurestep___pricingprocedurestep___pricingprocedurecounter___pricingprocedurecounter___ToSalesorder
GetASalesorderitemprelement_salesorder___salesorder___salesorderitem___salesorderitem___pricingprocedurestep___pricingprocedurestep___pricingprocedurecounter___pricingprocedurecounter___ToSalesorderitem
GetASalesorderitemrelatedobject
PostASalesorderitemrelatedobject
GetASalesorderitemrelatedobject_salesorder___salesorder___salesorderitem___salesorderitem___sddocrelatedobjectsequencenmbr___sddocrelatedobjectsequencenmbr___
DeleteASalesorderitemrelatedobject_salesorder___salesorder___salesorderitem___salesorderitem___sddocrelatedobjectsequencenmbr___sddocrelatedobjectsequencenmbr___
GetASalesorderitemrelatedobject_salesorder___salesorder___salesorderitem___salesorderitem___sddocrelatedobjectsequencenmbr___sddocrelatedobjectsequencenmbr___ToSalesorder
GetASalesorderitemrelatedobject_salesorder___salesorder___salesorderitem___salesorderitem___sddocrelatedobjectsequencenmbr___sddocrelatedobjectsequencenmbr___ToSalesorderitem
GetASalesorderitemtext
PostASalesorderitemtext
GetASalesorderitemtext_salesorder___salesorder___salesorderitem___salesorderitem___language___language___longtextid___longtextid___
DeleteASalesorderitemtext_salesorder___salesorder___salesorderitem___salesorderitem___language___language___longtextid___longtextid___
PatchASalesorderitemtext_salesorder___salesorder___salesorderitem___salesorderitem___language___language___longtextid___longtextid___
GetASalesorderitemtext_salesorder___salesorder___salesorderitem___salesorderitem___language___language___longtextid___longtextid___ToSalesorder
GetASalesorderitemtext_salesorder___salesorder___salesorderitem___salesorderitem___language___language___longtextid___longtextid___ToSalesorderitem
GetASalesorderitmprecdgprocflow
GetASalesorderitmprecdgprocflow_salesorder___salesorder___salesorderitem___salesorderitem___docrelationshipuuid_guid__docrelationshipuuid___
GetASalesorderitmprecdgprocflow_salesorder___salesorder___salesorderitem___salesorderitem___docrelationshipuuid_guid__docrelationshipuuid___ToSalesorder
GetASalesorderitmprecdgprocflow_salesorder___salesorder___salesorderitem___salesorderitem___docrelationshipuuid_guid__docrelationshipuuid___ToSalesorderitem
GetASalesorderitmsubsqntprocflow
GetASalesorderitmsubsqntprocflow_salesorder___salesorder___salesorderitem___salesorderitem___docrelationshipuuid_guid__docrelationshipuuid___
GetASalesorderitmsubsqntprocflow_salesorder___salesorder___salesorderitem___salesorderitem___docrelationshipuuid_guid__docrelationshipuuid___ToSalesorder
GetASalesorderitmsubsqntprocflow_salesorder___salesorder___salesorderitem___salesorderitem___docrelationshipuuid_guid__docrelationshipuuid___ToSalesorderitem
GetASalesorderpartneraddress
GetASalesorderpartneraddress_salesorder___salesorder___partnerfunction___partnerfunction___addressrepresentationcode___addressrepresentationcode___
PatchASalesorderpartneraddress_salesorder___salesorder___partnerfunction___partnerfunction___addressrepresentationcode___addressrepresentationcode___
GetASalesorderpartneraddress_salesorder___salesorder___partnerfunction___partnerfunction___addressrepresentationcode___addressrepresentationcode___ToPartner
GetASalesorderpartneraddress_salesorder___salesorder___partnerfunction___partnerfunction___addressrepresentationcode___addressrepresentationcode___ToSalesorder
GetASalesorderprecdgprocflow
GetASalesorderprecdgprocflow_salesorder___salesorder___docrelationshipuuid_guid__docrelationshipuuid___
GetASalesorderprecdgprocflow_salesorder___salesorder___docrelationshipuuid_guid__docrelationshipuuid___ToSalesorder
GetASalesorderrelatedobject
PostASalesorderrelatedobject
GetASalesorderrelatedobject_salesorder___salesorder___sddocrelatedobjectsequencenmbr___sddocrelatedobjectsequencenmbr___
DeleteASalesorderrelatedobject_salesorder___salesorder___sddocrelatedobjectsequencenmbr___sddocrelatedobjectsequencenmbr___
GetASalesorderrelatedobject_salesorder___salesorder___sddocrelatedobjectsequencenmbr___sddocrelatedobjectsequencenmbr___ToSalesorder
GetASalesorderscheduleline
PostASalesorderscheduleline
GetASalesorderscheduleline_salesorder___salesorder___salesorderitem___salesorderitem___scheduleline___scheduleline___
DeleteASalesorderscheduleline_salesorder___salesorder___salesorderitem___salesorderitem___scheduleline___scheduleline___
PatchASalesorderscheduleline_salesorder___salesorder___salesorderitem___salesorderitem___scheduleline___scheduleline___
GetASalesordersubsqntprocflow
GetASalesordersubsqntprocflow_salesorder___salesorder___docrelationshipuuid_guid__docrelationshipuuid___
GetASalesordersubsqntprocflow_salesorder___salesorder___docrelationshipuuid_guid__docrelationshipuuid___ToSalesorder
GetASalesordertext
PostASalesordertext
GetASalesordertext_salesorder___salesorder___language___language___longtextid___longtextid___
DeleteASalesordertext_salesorder___salesorder___language___language___longtextid___longtextid___
PatchASalesordertext_salesorder___salesorder___language___language___longtextid___longtextid___
GetASalesordertext_salesorder___salesorder___language___language___longtextid___longtextid___ToSalesorder
GetASlsorderitembillingplanitem
PostASlsorderitembillingplanitem
GetASlsorderitembillingplanitem_salesorder___salesorder___salesorderitem___salesorderitem___billingplan___billingplan___billingplanitem___billingplanitem___
DeleteASlsorderitembillingplanitem_salesorder___salesorder___salesorderitem___salesorderitem___billingplan___billingplan___billingplanitem___billingplanitem___
PatchASlsorderitembillingplanitem_salesorder___salesorder___salesorderitem___salesorderitem___billingplan___billingplan___billingplanitem___billingplanitem___
GetASlsorderitembillingplanitem_salesorder___salesorder___salesorderitem___salesorderitem___billingplan___billingplan___billingplanitem___billingplanitem___ToBillingplan
GetASlsorderitembillingplanitem_salesorder___salesorder___salesorderitem___salesorderitem___billingplan___billingplan___billingplanitem___billingplanitem___ToSalesorder
GetASlsorderitembillingplanitem_salesorder___salesorder___salesorderitem___salesorderitem___billingplan___billingplan___billingplanitem___billingplanitem___ToSalesorderitem
GetASlsordpaymentplanitemdetails
PostASlsordpaymentplanitemdetails
GetASlsordpaymentplanitemdetails_salesorder___salesorder___paymentplanitem___paymentplanitem___
DeleteASlsordpaymentplanitemdetails_salesorder___salesorder___paymentplanitem___paymentplanitem___
PatchASlsordpaymentplanitemdetails_salesorder___salesorder___paymentplanitem___paymentplanitem___
GetASlsordpaymentplanitemdetails_salesorder___salesorder___paymentplanitem___paymentplanitem___ToSalesorder
PostRejectapprovalrequest
PostReleaseapprovalrequest

```


Procedure

create a sales order by using tool 
PostASalesorder
body
```json
{
  "Salesorganization": "1710",
  "Distributionchannel": "10",
  "Organizationdivision": "00",
  "Soldtoparty": "17100003"
}
```
this step returned sales order number 6319. 

this creates the the sales order record without any item. Then we can add items to the sales order by using the tool
PostASalesorder___salesorder___ToItem
body
```json
{
  "Material": "PUMP_MOTOR_KE",
  "Requestedquantity": "2",
  "Requestedquantityunit": "PC",
  "Plant": "1710",
}
``` 
PUMP_MOTOR_KE has an item price of 835 USD 

Response: 

```json
{
  "d": {
    "__metadata": {
      "id": "http://34.95.14.112:50000/sap/opu/odata/sap/API_SALES_ORDER_SRV/A_SalesOrder('6319')",
      "uri": "http://34.95.14.112:50000/sap/opu/odata/sap/API_SALES_ORDER_SRV/A_SalesOrder('6319')",
      "type": "API_SALES_ORDER_SRV.A_SalesOrderType",
      "etag": "W/\"datetimeoffset'2026-04-18T20%3A23%3A29.5937010Z'\""
    },
    "SalesOrder": "6319",
    "SalesOrderType": "OR",
    "SalesOrganization": "1710",
    "DistributionChannel": "10",
    "OrganizationDivision": "00",
    "SalesGroup": "",
    "SalesOffice": "",
    "SalesDistrict": "",
    "SoldToParty": "17100003",
    "CreationDate": "/Date(1776470400000)/",
    "CreatedByUser": "BPINST",
    "LastChangeDate": "/Date(1776470400000)/",
    "SenderBusinessSystemName": "",
    "ExternalDocumentID": "",
    "LastChangeDateTime": "/Date(1776543809593+0000)/",
    "ExternalDocLastChangeDateTime": null,
    "PurchaseOrderByCustomer": "",
    "PurchaseOrderByShipToParty": "17100003",
    "CustomerPurchaseOrderType": "",
    "CustomerPurchaseOrderDate": null,
    "SalesOrderDate": "/Date(1776470400000)/",
    "TotalNetAmount": "1670.00",
    "OverallDeliveryStatus": "A",
    "TotalBlockStatus": "",
    "OverallOrdReltdBillgStatus": "",
    "OverallSDDocReferenceStatus": "",
    "TransactionCurrency": "USD",
    "SDDocumentReason": "",
    "PricingDate": "/Date(1776470400000)/",
    "PriceDetnExchangeRate": "1.00000",
    "PaymentGuaranteeProcedure": "000002",
    "BillingPlan": "",
    "RequestedDeliveryDate": "/Date(1776470400000)/",
    "ShippingCondition": "01",
    "CompleteDeliveryIsDefined": false,
    "ShippingType": "",
    "HeaderBillingBlockReason": "",
    "DeliveryBlockReason": "",
    "DeliveryDateTypeRule": "",
    "IncotermsClassification": "EXW",
    "IncotermsTransferLocation": "Palo Alto",
    "IncotermsLocation1": "Palo Alto",
    "IncotermsLocation2": "",
    "IncotermsVersion": "",
    "CustomerPriceGroup": "",
    "PriceListType": "",
    "CustomerPaymentTerms": "0004",
    "PaymentMethod": "",
    "FixedValueDate": null,
    "AssignmentReference": "",
    "ReferenceSDDocument": "",
    "ReferenceSDDocumentCategory": "",
    "AccountingDocExternalReference": "",
    "CustomerAccountAssignmentGroup": "01",
    "AccountingExchangeRate": "0.00000",
    "CorrespncExternalReference": "",
    "SlsDocSo2PLastContactPersnName": "",
    "SlsDocSo2PLstCntctPersnTelNmbr": "999-654-2356",
    "POCorrespncExternalReference": "",
    "CustomerConditionGroup1": "",
    "CustomerConditionGroup2": "",
    "CustomerConditionGroup3": "",
    "CustomerConditionGroup4": "",
    "CustomerConditionGroup5": "",
    "CustomerGroup": "01",
    "AdditionalCustomerGroup1": "",
    "AdditionalCustomerGroup2": "",
    "AdditionalCustomerGroup3": "",
    "AdditionalCustomerGroup4": "",
    "AdditionalCustomerGroup5": "",
    "SlsDocIsRlvtForProofOfDeliv": true,
    "CustomerTaxClassification1": "",
    "CustomerTaxClassification2": "",
    "CustomerTaxClassification3": "",
    "CustomerTaxClassification4": "",
    "CustomerTaxClassification5": "",
    "CustomerTaxClassification6": "",
    "CustomerTaxClassification7": "",
    "CustomerTaxClassification8": "",
    "CustomerTaxClassification9": "",
    "TaxDepartureCountry": "",
    "VATRegistrationCountry": "",
    "SalesOrderApprovalReason": "",
    "SalesDocApprovalStatus": "",
    "OverallSDProcessStatus": "A",
    "TotalCreditCheckStatus": "",
    "OverallTotalDeliveryStatus": "A",
    "OverallSDDocumentRejectionSts": "A",
    "BillingDocumentDate": "/Date(1776470400000)/",
    "ContractAccount": "",
    "AdditionalValueDays": "0",
    "CustomerPurchaseOrderSuplmnt": "",
    "ServicesRenderedDate": null,
    "to_BillingPlan": {
      "__deferred": {
        "uri": "http://34.95.14.112:50000/sap/opu/odata/sap/API_SALES_ORDER_SRV/A_SalesOrder('6319')/to_BillingPlan"
      }
    },
    "to_Item": {
      "__deferred": {
        "uri": "http://34.95.14.112:50000/sap/opu/odata/sap/API_SALES_ORDER_SRV/A_SalesOrder('6319')/to_Item"
      }
    },
    "to_Partner": {
      "__deferred": {
        "uri": "http://34.95.14.112:50000/sap/opu/odata/sap/API_SALES_ORDER_SRV/A_SalesOrder('6319')/to_Partner"
      }
    },
    "to_PaymentPlanItemDetails": {
      "__deferred": {
        "uri": "http://34.95.14.112:50000/sap/opu/odata/sap/API_SALES_ORDER_SRV/A_SalesOrder('6319')/to_PaymentPlanItemDetails"
      }
    },
    "to_PrecedingProcFlowDoc": {
      "__deferred": {
        "uri": "http://34.95.14.112:50000/sap/opu/odata/sap/API_SALES_ORDER_SRV/A_SalesOrder('6319')/to_PrecedingProcFlowDoc"
      }
    },
    "to_PricingElement": {
      "__deferred": {
        "uri": "http://34.95.14.112:50000/sap/opu/odata/sap/API_SALES_ORDER_SRV/A_SalesOrder('6319')/to_PricingElement"
      }
    },
    "to_RelatedObject": {
      "__deferred": {
        "uri": "http://34.95.14.112:50000/sap/opu/odata/sap/API_SALES_ORDER_SRV/A_SalesOrder('6319')/to_RelatedObject"
      }
    },
    "to_SubsequentProcFlowDoc": {
      "__deferred": {
        "uri": "http://34.95.14.112:50000/sap/opu/odata/sap/API_SALES_ORDER_SRV/A_SalesOrder('6319')/to_SubsequentProcFlowDoc"
      }
    },
    "to_Text": {
      "__deferred": {
        "uri": "http://34.95.14.112:50000/sap/opu/odata/sap/API_SALES_ORDER_SRV/A_SalesOrder('6319')/to_Text"
      }
    }
  }
}

```



apply a discount and shipping fees to the sales order 6319 using 