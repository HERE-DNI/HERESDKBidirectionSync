---
title: "ChargingConnectorAttributes (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-chargingconnectorattributes"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-com-here-sdk-routing-package-summary">com.here.sdk.routing</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.routing.ChargingConnectorAttributes → com.here.sdk.routing.ChargingConnectorAttributes

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">ChargingConnectorAttributes</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Details of the connector that is suggested to be used in the section's PostAction 's for charging.

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

  <a href="sdk-for-android-explore-com-here-sdk-routing-chargingconnectortype" title="enum class in com.here.sdk.routing">`ChargingConnectorType`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-chargingconnectorattributes#connectorType" class="member-name-link"><code>connectorType</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Suggested connector for charging at this station.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-chargingconnectorattributes#currentInAmperes" class="member-name-link"><code>currentInAmperes</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Current of the suggested connector in Amperes.

  </div>

  </div>

  <div class="col-first even-row-color">

  `double`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-chargingconnectorattributes#powerInKilowatts" class="member-name-link"><code>powerInKilowatts</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Power supplied by the suggested connector in kW.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-chargingsupplytype" title="enum class in com.here.sdk.routing">`ChargingSupplyType`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-chargingconnectorattributes#supplyType" class="member-name-link"><code>supplyType</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Supply type of the suggested connector.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-chargingconnectorattributes#voltageInVolts" class="member-name-link"><code>voltageInVolts</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Voltage of the suggested connector in Volts.

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

      ChargingConnectorAttributes (double powerInKilowatts, Double currentInAmperes, Double voltageInVolts, ChargingSupplyType supplyType, ChargingConnectorType connectorType)

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

  - <div id="sdk-for-android-explore-powerInKilowatts" class="section detail">

    ### powerInKilowatts

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">powerInKilowatts</span>

    </div>

    <div class="block">

    Power supplied by the suggested connector in kW.

    </div>

    </div>

  - <div id="sdk-for-android-explore-currentInAmperes" class="section detail">

    ### currentInAmperes

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">currentInAmperes</span>

    </div>

    <div class="block">

    Current of the suggested connector in Amperes.

    </div>

    </div>

  - <div id="sdk-for-android-explore-voltageInVolts" class="section detail">

    ### voltageInVolts

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">voltageInVolts</span>

    </div>

    <div class="block">

    Voltage of the suggested connector in Volts.

    </div>

    </div>

  - <div id="sdk-for-android-explore-supplyType" class="section detail">

    ### supplyType

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-routing-chargingsupplytype" title="enum class in com.here.sdk.routing">ChargingSupplyType</a></span> <span class="element-name">supplyType</span>

    </div>

    <div class="block">

    Supply type of the suggested connector.

    </div>

    </div>

  - <div id="sdk-for-android-explore-connectorType" class="section detail">

    ### connectorType

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-routing-chargingconnectortype" title="enum class in com.here.sdk.routing">ChargingConnectorType</a></span> <span class="element-name">connectorType</span>

    </div>

    <div class="block">

    Suggested connector for charging at this station.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-explore-init-double-java-lang-Double-java-lang-Double-com-here-sdk-routing-ChargingSupplyType-com-here-sdk-routing-ChargingConnectorType" class="section detail">

    ### ChargingConnectorAttributes

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">ChargingConnectorAttributes</span><wbr></wbr><span class="parameters">(double powerInKilowatts, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a> currentInAmperes, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a> voltageInVolts, @Nullable <a href="sdk-for-android-explore-com-here-sdk-routing-chargingsupplytype" title="enum class in com.here.sdk.routing">ChargingSupplyType</a> supplyType, @Nullable <a href="sdk-for-android-explore-com-here-sdk-routing-chargingconnectortype" title="enum class in com.here.sdk.routing">ChargingConnectorType</a> connectorType)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `powerInKilowatts` -

    Power supplied by the suggested connector in kW.

    `currentInAmperes` -

    Current of the suggested connector in Amperes.

    `voltageInVolts` -

    Voltage of the suggested connector in Volts.

    `supplyType` -

    Supply type of the suggested connector.

    `connectorType` -

    Suggested connector for charging at this station.

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

