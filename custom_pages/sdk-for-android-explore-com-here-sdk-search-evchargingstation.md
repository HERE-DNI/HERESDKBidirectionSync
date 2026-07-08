---
title: "EVChargingStation (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-search-evchargingstation"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.search](sdk-for-android-explore-com-here-sdk-search-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.search.EVChargingStation → com.here.sdk.search.EVChargingStation

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">EVChargingStation</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Group of connectors for electric vehicles (EVs), defined by a common charging connector type and maximum power level. Use PlaceCategory.BUSINESS_AND_SERVICES_EV_CHARGING_STATION to find stations. In the Details of a Place result you can find the list of found pools containing stations, if any. For offline EV rich attributes, enable LayerConfiguration.Feature.EV in SDKOptions.layerConfiguration .

</div>

</div>

- <div id="sdk-for-android-explore-field-summary" class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Field

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evchargingstation#availableConnectorCount" class="member-name-link"><code>availableConnectorCount</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Number of available physical connectors at the charging station.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evchargingstation#chargingMode" class="member-name-link"><code>chargingMode</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Charging mode of the charging station.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evchargingstation#connectorCount" class="member-name-link"><code>connectorCount</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Number of physical connectors at the charging station.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evchargingstation#connectorTypeId" class="member-name-link"><code>connectorTypeId</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  ID of the connector type.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evchargingstation#connectorTypeName" class="member-name-link"><code>connectorTypeName</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Name of the connector type.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evchargingstation#currentRangeInAmperes" class="member-name-link"><code>currentRangeInAmperes</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Current range provided by the charging station, in amperes.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" class="external-link" title="class or interface in java.lang"><code>Boolean</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evchargingstation#hasFixedCable" class="member-name-link"><code>hasFixedCable</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Indicates that the cable is fixed or not fixed for a specific Connector Type on the charge station.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util"><code>Date</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evchargingstation#lastUpdated" class="member-name-link"><code>lastUpdated</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Last update of the available_connector_count and occupied_connector_count fields.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evchargingstation#maxPowerInKilowatts" class="member-name-link"><code>maxPowerInKilowatts</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Maximum charge power of connectors in kW.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evchargingstation#occupiedConnectorCount" class="member-name-link"><code>occupiedConnectorCount</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Number of occupied physical connectors at the charging station.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evchargingstation#outOfServiceConnectorCount" class="member-name-link"><code>outOfServiceConnectorCount</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Number of physical connectors that are out of service at the charging station.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evchargingstation#phaseCount" class="member-name-link"><code>phaseCount</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Number of phases used by the charging station.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evchargingstation#physicalReference" class="member-name-link"><code>physicalReference</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Printed on the outside of the EVSE for visual identification.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evchargingstation#powerFeedTypeId" class="member-name-link"><code>powerFeedTypeId</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  ID of the power feed type, as defined by the https://en.wikipedia.org/wiki/SAE_J1772#Charging standard.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evchargingstation#powerFeedTypeName" class="member-name-link"><code>powerFeedTypeName</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Name of the power feed type, as defined by the https://en.wikipedia.org/wiki/SAE_J1772#Charging standard.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evchargingstation#reservedConnectorCount" class="member-name-link"><code>reservedConnectorCount</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Number of physical connectors that are reserved at the charging station.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evchargingstation#supplierName" class="member-name-link"><code>supplierName</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The EV charging station operator.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evchargingstation#voltageRangeInVolts" class="member-name-link"><code>voltageRangeInVolts</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Voltage range of the charge provided by the charging station, in volts.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-constructor-summary" class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Constructor

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-constructor-name even-row-color">

      EVChargingStation ()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary" class="section method-summary">

  <div id="sdk-for-android-explore-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      equals ( Object obj)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-field-detail" class="section field-details">

  - <div id="sdk-for-android-explore-supplierName" class="section detail">

    ### supplierName

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">supplierName</span>

    </div>

    <div class="block">

    The EV charging station operator. This field is always null for offline search using the OfflineSearchEngine . For online search using the SearchEngine , it can be null if data is unavailable.

    </div>

    </div>

  - <div id="sdk-for-android-explore-connectorTypeName" class="section detail">

    ### connectorTypeName

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">connectorTypeName</span>

    </div>

    <div class="block">

    Name of the connector type. For more information on the current connector types, see https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-type-connector.html May include customer-facing names. In such cases, a 'customer names' label is present. This field can be null if data is unavailable.

    </div>

    </div>

  - <div id="sdk-for-android-explore-connectorTypeId" class="section detail">

    ### connectorTypeId

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">connectorTypeId</span>

    </div>

    <div class="block">

    ID of the connector type. For more information on the current connector types, see https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-type-connector.html This field is always null for offline search using the OfflineSearchEngine . For online searches using the SearchEngine , it may be null if the data is unavailable.

    </div>

    </div>

  - <div id="sdk-for-android-explore-powerFeedTypeName" class="section detail">

    ### powerFeedTypeName

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">powerFeedTypeName</span>

    </div>

    <div class="block">

    Name of the power feed type, as defined by the https://en.wikipedia.org/wiki/SAE_J1772#Charging standard. Provides the customer information on the charge level of the specific Connector Type. Also, can describe level that is used in North America and Australia. In that case label 'North America (Australia)' is present. This field can be null if data is unavailable.

    </div>

    </div>

  - <div id="sdk-for-android-explore-powerFeedTypeId" class="section detail">

    ### powerFeedTypeId

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">powerFeedTypeId</span>

    </div>

    <div class="block">

    ID of the power feed type, as defined by the https://en.wikipedia.org/wiki/SAE_J1772#Charging standard. No data in case of offline search. This field is always null for offline search using the OfflineSearchEngine . For online searches using the SearchEngine , it may be null if the data is unavailable.

    </div>

    </div>

  - <div id="sdk-for-android-explore-maxPowerInKilowatts" class="section detail">

    ### maxPowerInKilowatts

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">maxPowerInKilowatts</span>

    </div>

    <div class="block">

    Maximum charge power of connectors in kW. This field can be null if data is unavailable.

    </div>

    </div>

  - <div id="sdk-for-android-explore-connectorCount" class="section detail">

    ### connectorCount

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a></span> <span class="element-name">connectorCount</span>

    </div>

    <div class="block">

    Number of physical connectors at the charging station. This field can be null if data is unavailable.

    </div>

    </div>

  - <div id="sdk-for-android-explore-availableConnectorCount" class="section detail">

    ### availableConnectorCount

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a></span> <span class="element-name">availableConnectorCount</span>

    </div>

    <div class="block">

    Number of available physical connectors at the charging station. This field is always null for offline search using the OfflineSearchEngine . For online searches using the SearchEngine , it may be null if the data is unavailable.

    </div>

    </div>

  - <div id="sdk-for-android-explore-occupiedConnectorCount" class="section detail">

    ### occupiedConnectorCount

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a></span> <span class="element-name">occupiedConnectorCount</span>

    </div>

    <div class="block">

    Number of occupied physical connectors at the charging station. This field is always null for offline search using the OfflineSearchEngine . For online searches using the SearchEngine , it may be null if the data is unavailable.

    </div>

    </div>

  - <div id="sdk-for-android-explore-outOfServiceConnectorCount" class="section detail">

    ### outOfServiceConnectorCount

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a></span> <span class="element-name">outOfServiceConnectorCount</span>

    </div>

    <div class="block">

    Number of physical connectors that are out of service at the charging station. This field is always null for offline search using the OfflineSearchEngine . For online searches using the SearchEngine , it may be null if the data is unavailable.

    </div>

    </div>

  - <div id="sdk-for-android-explore-reservedConnectorCount" class="section detail">

    ### reservedConnectorCount

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a></span> <span class="element-name">reservedConnectorCount</span>

    </div>

    <div class="block">

    Number of physical connectors that are reserved at the charging station. This field is always null for offline search using the OfflineSearchEngine . For online searches using the SearchEngine , it may be null if the data is unavailable.

    </div>

    </div>

  - <div id="sdk-for-android-explore-lastUpdated" class="section detail">

    ### lastUpdated

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util">Date</a></span> <span class="element-name">lastUpdated</span>

    </div>

    <div class="block">

    Last update of the available_connector_count and occupied_connector_count fields. This field is always null for offline search using the OfflineSearchEngine . For online searches using the SearchEngine , it may be null if the data is unavailable.

    </div>

    </div>

  - <div id="sdk-for-android-explore-chargingMode" class="section detail">

    ### chargingMode

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">chargingMode</span>

    </div>

    <div class="block">

    Charging mode of the charging station. For more information, see https://en.wikipedia.org/w/index.php?title=Charging_station&oldid=1013010605#IEC-61851-1_Charging_Modes standard. This field can be null if data is unavailable.

    </div>

    </div>

  - <div id="sdk-for-android-explore-voltageRangeInVolts" class="section detail">

    ### voltageRangeInVolts

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">voltageRangeInVolts</span>

    </div>

    <div class="block">

    Voltage range of the charge provided by the charging station, in volts. Values are alphanumeric represented by the voltage range followed by 'V' and by the current type 'AC' or 'DC', for example: '100-120V AC'. This field can be null if data is unavailable.

    </div>

    </div>

  - <div id="sdk-for-android-explore-currentRangeInAmperes" class="section detail">

    ### currentRangeInAmperes

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">currentRangeInAmperes</span>

    </div>

    <div class="block">

    Current range provided by the charging station, in amperes. Values are alphanumeric represented by the Ampere value followed by an 'A', for example '12A-80A'. This field can be null if data is unavailable.

    </div>

    </div>

  - <div id="sdk-for-android-explore-phaseCount" class="section detail">

    ### phaseCount

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a></span> <span class="element-name">phaseCount</span>

    </div>

    <div class="block">

    Number of phases used by the charging station. This field can be null if data is unavailable.

    </div>

    </div>

  - <div id="sdk-for-android-explore-hasFixedCable" class="section detail">

    ### hasFixedCable

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" class="external-link" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">hasFixedCable</span>

    </div>

    <div class="block">

    Indicates that the cable is fixed or not fixed for a specific Connector Type on the charge station. This field can be null if data is unavailable.

    </div>

    </div>

  - <div id="sdk-for-android-explore-physicalReference" class="section detail">

    ### physicalReference

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">physicalReference</span>

    </div>

    <div class="block">

    Printed on the outside of the EVSE for visual identification. Available only in offline search. This field can be null if data is unavailable.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-explore-init" class="section detail">

    ### EVChargingStation

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">EVChargingStation</span>()

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-equals-java-lang-Object" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-explore-hashCode" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

