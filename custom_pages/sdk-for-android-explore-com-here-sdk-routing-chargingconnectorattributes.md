---
title: "ChargingConnectorAttributes (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-chargingconnectorattributes"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.routing.ChargingConnectorAttributes

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">ChargingConnectorAttributes</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Details of the connector that is suggested to be used in the section's
PostAction 's for charging.

</div>

</div>

<div class="section summary">

- <div id="field-summary" class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Field</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-chargingconnectortype"
  title="enum class in com.here.sdk.routing"><code>ChargingConnectorType</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-chargingconnectorattributes#connectorType"
  class="member-name-link"><code>connectorType</code></a></td>
  <td><div class="block">
  Suggested connector for charging at this station.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-chargingconnectorattributes#currentInAmperes"
  class="member-name-link"><code>currentInAmperes</code></a></td>
  <td><div class="block">
  Current of the suggested connector in Amperes.
  </div></td>
  </tr>
  <tr>
  <td><code>double</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-chargingconnectorattributes#powerInKilowatts"
  class="member-name-link"><code>powerInKilowatts</code></a></td>
  <td><div class="block">
  Power supplied by the suggested connector in kW.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-chargingsupplytype"
  title="enum class in com.here.sdk.routing"><code>ChargingSupplyType</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-chargingconnectorattributes#supplyType"
  class="member-name-link"><code>supplyType</code></a></td>
  <td><div class="block">
  Supply type of the suggested connector.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-chargingconnectorattributes#voltageInVolts"
  class="member-name-link"><code>voltageInVolts</code></a></td>
  <td><div class="block">
  Voltage of the suggested connector in Volts.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="constructor-summary" class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <table>
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <thead>
  <tr>
  <th>Constructor</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><pre><code>ChargingConnectorAttributes(double powerInKilowatts,
   Double currentInAmperes,
   Double voltageInVolts,
   ChargingSupplyType supplyType,
   ChargingConnectorType connectorType)</code></pre></td>
  <td><div class="block">
  Creates a new instance.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Instance Methods
  Concrete Methods

  </div>

  <div id="method-summary-table.tabpanel"
  aria-labelledby="method-summary-table-tab0" role="tabpanel">

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Method</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>boolean</code></td>
  <td><pre><code>equals(Object obj)</code></pre></td>
  <td> </td>
  </tr>
  <tr>
  <td><code>int</code></td>
  <td><pre><code>hashCode()</code></pre></td>
  <td> </td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="field-detail" class="section field-details">

  - <div id="powerInKilowatts" class="section detail">

    ### powerInKilowatts

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">powerInKilowatts</span>

    </div>

    <div class="block">

    Power supplied by the suggested connector in kW.

    </div>

    </div>

  - <div id="currentInAmperes" class="section detail">

    ### currentInAmperes

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">currentInAmperes</span>

    </div>

    <div class="block">

    Current of the suggested connector in Amperes.

    </div>

    </div>

  - <div id="voltageInVolts" class="section detail">

    ### voltageInVolts

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">voltageInVolts</span>

    </div>

    <div class="block">

    Voltage of the suggested connector in Volts.

    </div>

    </div>

  - <div id="supplyType" class="section detail">

    ### supplyType

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[ChargingSupplyType](sdk-for-android-explore-com-here-sdk-routing-chargingsupplytype "enum class in com.here.sdk.routing")</span> <span class="element-name">supplyType</span>

    </div>

    <div class="block">

    Supply type of the suggested connector.

    </div>

    </div>

  - <div id="connectorType" class="section detail">

    ### connectorType

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[ChargingConnectorType](sdk-for-android-explore-com-here-sdk-routing-chargingconnectortype "enum class in com.here.sdk.routing")</span> <span class="element-name">connectorType</span>

    </div>

    <div class="block">

    Suggested connector for charging at this station.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(double,java.lang.Double,java.lang.Double,com.here.sdk.routing.ChargingSupplyType,com.here.sdk.routing.ChargingConnectorType)"
    class="section detail">

    ### ChargingConnectorAttributes

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">ChargingConnectorAttributes</span><span class="parameters">(double powerInKilowatts,
    @Nullable <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a> currentInAmperes,
    @Nullable <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a> voltageInVolts,
    @Nullable
    [ChargingSupplyType](sdk-for-android-explore-com-here-sdk-routing-chargingsupplytype "enum class in com.here.sdk.routing") supplyType,
    @Nullable
    [ChargingConnectorType](sdk-for-android-explore-com-here-sdk-routing-chargingconnectortype "enum class in com.here.sdk.routing") connectorType)</span>

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

- <div id="method-detail" class="section method-details">

  - <div id="equals(java.lang.Object)" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><span class="parameters">(<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
    class="external-link"
    title="class or interface in java.lang"><code>equals</code></a> in
    class <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link"
    title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="hashCode()" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
    class="external-link"
    title="class or interface in java.lang"><code>hashCode</code></a> in
    class <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link"
    title="class or interface in java.lang"><code>Object</code></a>

    </div>

  </div>

</div>

