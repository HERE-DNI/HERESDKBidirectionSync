---
title: "ChargingStation (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-chargingstation"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-com-here-sdk-routing-package-summary">com.here.sdk.routing</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.routing.ChargingStation → com.here.sdk.routing.ChargingStation

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">ChargingStation</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Data for an electric vehicle charging station.

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

  <a href="sdk-for-android-explore-com-here-sdk-core-nameid" title="class in com.here.sdk.core">`NameID`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-chargingstation#brand" class="member-name-link"><code>brand</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Charging station brand.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-core-nameid" title="class in com.here.sdk.core">`NameID`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-chargingstation#chargePointOperator" class="member-name-link"><code>chargePointOperator</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Charging station charge-point-operator.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-chargingconnectorattributes" title="class in com.here.sdk.routing">`ChargingConnectorAttributes`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-chargingstation#connectorAttributes" class="member-name-link"><code>connectorAttributes</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Details of the connector suggested to be used.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-chargingstation#id" class="member-name-link"><code>id</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Identifier of this charging station.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-explore-com-here-sdk-core-nameid" title="class in com.here.sdk.core">`NameID`</a>`>`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-chargingstation#matchingEMobilityServiceProviders" class="member-name-link"><code>matchingEMobilityServiceProviders</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  List of matched E-Mobility Service Providers.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-chargingstation#name" class="member-name-link"><code>name</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Human readable name of this charging station.

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

      ChargingStation ( String id, String name, ChargingConnectorAttributes connectorAttributes)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      ChargingStation ( String id, String name, ChargingConnectorAttributes connectorAttributes, NameID brand, NameID chargePointOperator, List < NameID > matchingEMobilityServiceProviders)

  </div>

  <div class="col-last odd-row-color">

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

  - <div id="sdk-for-android-explore-id" class="section detail">

    ### id

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">id</span>

    </div>

    <div class="block">

    Identifier of this charging station. It can only be null when custom charging stations from non-HERE datasets have been injected on the HERE platform. By default, with HERE datasets it is guranteed to be not null.

    </div>

    </div>

  - <div id="sdk-for-android-explore-name" class="section detail">

    ### name

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">name</span>

    </div>

    <div class="block">

    Human readable name of this charging station. It can be null when there is no name associated with the station.

    </div>

    </div>

  - <div id="sdk-for-android-explore-connectorAttributes" class="section detail">

    ### connectorAttributes

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-routing-chargingconnectorattributes" title="class in com.here.sdk.routing">ChargingConnectorAttributes</a></span> <span class="element-name">connectorAttributes</span>

    </div>

    <div class="block">

    Details of the connector suggested to be used.

    </div>

    </div>

  - <div id="sdk-for-android-explore-brand" class="section detail">

    ### brand

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-core-nameid" title="class in com.here.sdk.core">NameID</a></span> <span class="element-name">brand</span>

    </div>

    <div class="block">

    Charging station brand. NameID.name reflect to charging station brand name. NameID.id reflect to charging station brand unique ID.

    </div>

    </div>

  - <div id="sdk-for-android-explore-chargePointOperator" class="section detail">

    ### chargePointOperator

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-core-nameid" title="class in com.here.sdk.core">NameID</a></span> <span class="element-name">chargePointOperator</span>

    </div>

    <div class="block">

    Charging station charge-point-operator. NameID.name reflect to charge-point-operator name. NameID.id reflect to charge-point-operator ID.

    </div>

    </div>

  - <div id="sdk-for-android-explore-matchingEMobilityServiceProviders" class="section detail">

    ### matchingEMobilityServiceProviders

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-explore-com-here-sdk-core-nameid" title="class in com.here.sdk.core">NameID</a>\></span> <span class="element-name">matchingEMobilityServiceProviders</span>

    </div>

    <div class="block">

    List of matched E-Mobility Service Providers. Populated only when ElectricVehicleOptions.evMobilityServiceProviderPreferences was set. This list reflects the subset of E-Mobility Service Providers supported by the charging station, from the list specified in the request parameter ElectricVehicleOptions.evMobilityServiceProviderPreferences . NameID.name in each list item reflect to E-Mobility Service Provider name. NameID.id in each list item reflect to E-Mobility Service Provider id.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-explore-init-java-lang-String-java-lang-String-com-here-sdk-routing-ChargingConnectorAttributes" class="section detail">

    ### ChargingStation

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">ChargingStation</span><wbr></wbr><span class="parameters">(@Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> id, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> name, @Nullable <a href="sdk-for-android-explore-com-here-sdk-routing-chargingconnectorattributes" title="class in com.here.sdk.routing">ChargingConnectorAttributes</a> connectorAttributes)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `id` -

    Identifier of this charging station. It can only be null when custom charging stations from non-HERE datasets have been injected on the HERE platform. By default, with HERE datasets it is guranteed to be not null.

    `name` -

    Human readable name of this charging station. It can be null when there is no name associated with the station.

    `connectorAttributes` -

    Details of the connector suggested to be used.

    </div>

  - <div id="sdk-for-android-explore-init-java-lang-String-java-lang-String-com-here-sdk-routing-ChargingConnectorAttributes-com-here-sdk-core-NameID-com-here-sdk-core-NameID-java-util-List" class="section detail">

    ### ChargingStation

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">ChargingStation</span><wbr></wbr><span class="parameters">(@Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> id, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> name, @Nullable <a href="sdk-for-android-explore-com-here-sdk-routing-chargingconnectorattributes" title="class in com.here.sdk.routing">ChargingConnectorAttributes</a> connectorAttributes, @Nullable <a href="sdk-for-android-explore-com-here-sdk-core-nameid" title="class in com.here.sdk.core">NameID</a> brand, @Nullable <a href="sdk-for-android-explore-com-here-sdk-core-nameid" title="class in com.here.sdk.core">NameID</a> chargePointOperator, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-explore-com-here-sdk-core-nameid" title="class in com.here.sdk.core">NameID</a>\> matchingEMobilityServiceProviders)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `id` -

    Identifier of this charging station. It can only be null when custom charging stations from non-HERE datasets have been injected on the HERE platform. By default, with HERE datasets it is guranteed to be not null.

    `name` -

    Human readable name of this charging station. It can be null when there is no name associated with the station.

    `connectorAttributes` -

    Details of the connector suggested to be used.

    `brand` -

    Charging station brand. <a href="sdk-for-android-explore-com-here-sdk-core-nameid#name">`NameID.name`</a> reflect to charging station brand name. <a href="sdk-for-android-explore-com-here-sdk-core-nameid#id">`NameID.id`</a> reflect to charging station brand unique ID.

    `chargePointOperator` -

    Charging station charge-point-operator. <a href="sdk-for-android-explore-com-here-sdk-core-nameid#name">`NameID.name`</a> reflect to charge-point-operator name. <a href="sdk-for-android-explore-com-here-sdk-core-nameid#id">`NameID.id`</a> reflect to charge-point-operator ID.

    `matchingEMobilityServiceProviders` -

    List of matched E-Mobility Service Providers. Populated only when <a href="sdk-for-android-explore-com-here-sdk-routing-electricvehicleoptions#evMobilityServiceProviderPreferences">`ElectricVehicleOptions.evMobilityServiceProviderPreferences`</a> was set. This list reflects the subset of E-Mobility Service Providers supported by the charging station, from the list specified in the request parameter <a href="sdk-for-android-explore-com-here-sdk-routing-electricvehicleoptions#evMobilityServiceProviderPreferences">`ElectricVehicleOptions.evMobilityServiceProviderPreferences`</a>. <a href="sdk-for-android-explore-com-here-sdk-core-nameid#name">`NameID.name`</a> in each list item reflect to E-Mobility Service Provider name. <a href="sdk-for-android-explore-com-here-sdk-core-nameid#id">`NameID.id`</a> in each list item reflect to E-Mobility Service Provider id.

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

