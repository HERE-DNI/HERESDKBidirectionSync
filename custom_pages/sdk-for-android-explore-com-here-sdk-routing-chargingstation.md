---
title: "ChargingStation (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-chargingstation"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.routing.ChargingStation

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">ChargingStation</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Data for an electric vehicle charging station.

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
  <td><a href="sdk-for-android-explore-com-here-sdk-core-nameid"
  title="class in com.here.sdk.core"><code>NameID</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-chargingstation#brand"
  class="member-name-link"><code>brand</code></a></td>
  <td><div class="block">
  Charging station brand.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-nameid"
  title="class in com.here.sdk.core"><code>NameID</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-chargingstation#chargePointOperator"
  class="member-name-link"><code>chargePointOperator</code></a></td>
  <td><div class="block">
  Charging station charge-point-operator.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-chargingconnectorattributes"
  title="class in com.here.sdk.routing"><code>ChargingConnectorAttributes</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-chargingstation#connectorAttributes"
  class="member-name-link"><code>connectorAttributes</code></a></td>
  <td><div class="block">
  Details of the connector suggested to be used.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-chargingstation#id"
  class="member-name-link"><code>id</code></a></td>
  <td><div class="block">
  Identifier of this charging station.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-core-nameid"
  title="class in com.here.sdk.core"><code>NameID</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-chargingstation#matchingEMobilityServiceProviders"
  class="member-name-link"><code>matchingEMobilityServiceProviders</code></a></td>
  <td><div class="block">
  List of matched E-Mobility Service Providers.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-chargingstation#name"
  class="member-name-link"><code>name</code></a></td>
  <td><div class="block">
  Human readable name of this charging station.
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
  <td><pre><code>ChargingStation(String id,
   String name,
   ChargingConnectorAttributes connectorAttributes)</code></pre></td>
  <td><div class="block">
  Creates a new instance.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>ChargingStation(String id,
   String name,
   ChargingConnectorAttributes connectorAttributes,
   NameID brand,
   NameID chargePointOperator,
   List&lt;NameID&gt; matchingEMobilityServiceProviders)</code></pre></td>
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

  - <div id="id" class="section detail">

    ### id

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">id</span>

    </div>

    <div class="block">

    Identifier of this charging station. It can only be null when custom
    charging stations from non-HERE datasets have been injected on the
    HERE platform. By default, with HERE datasets it is guranteed to be
    not null.

    </div>

    </div>

  - <div id="name" class="section detail">

    ### name

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">name</span>

    </div>

    <div class="block">

    Human readable name of this charging station. It can be null when
    there is no name associated with the station.

    </div>

    </div>

  - <div id="connectorAttributes" class="section detail">

    ### connectorAttributes

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[ChargingConnectorAttributes](sdk-for-android-explore-com-here-sdk-routing-chargingconnectorattributes "class in com.here.sdk.routing")</span> <span class="element-name">connectorAttributes</span>

    </div>

    <div class="block">

    Details of the connector suggested to be used.

    </div>

    </div>

  - <div id="brand" class="section detail">

    ### brand

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[NameID](sdk-for-android-explore-com-here-sdk-core-nameid "class in com.here.sdk.core")</span> <span class="element-name">brand</span>

    </div>

    <div class="block">

    Charging station brand. NameID.name reflect to charging station
    brand name. NameID.id reflect to charging station brand unique ID.

    </div>

    </div>

  - <div id="chargePointOperator" class="section detail">

    ### chargePointOperator

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[NameID](sdk-for-android-explore-com-here-sdk-core-nameid "class in com.here.sdk.core")</span> <span class="element-name">chargePointOperator</span>

    </div>

    <div class="block">

    Charging station charge-point-operator. NameID.name reflect to
    charge-point-operator name. NameID.id reflect to
    charge-point-operator ID.

    </div>

    </div>

  - <div id="matchingEMobilityServiceProviders" class="section detail">

    ### matchingEMobilityServiceProviders

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[NameID](sdk-for-android-explore-com-here-sdk-core-nameid "class in com.here.sdk.core")></span> <span class="element-name">matchingEMobilityServiceProviders</span>

    </div>

    <div class="block">

    List of matched E-Mobility Service Providers. Populated only when
    ElectricVehicleOptions.evMobilityServiceProviderPreferences was set.
    This list reflects the subset of E-Mobility Service Providers
    supported by the charging station, from the list specified in the
    request parameter
    ElectricVehicleOptions.evMobilityServiceProviderPreferences .
    NameID.name in each list item reflect to E-Mobility Service Provider
    name. NameID.id in each list item reflect to E-Mobility Service
    Provider id.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(java.lang.String,java.lang.String,com.here.sdk.routing.ChargingConnectorAttributes)"
    class="section detail">

    ### ChargingStation

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">ChargingStation</span><span class="parameters">(@Nullable
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> id,
    @Nullable <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> name,
    @Nullable
    [ChargingConnectorAttributes](sdk-for-android-explore-com-here-sdk-routing-chargingconnectorattributes "class in com.here.sdk.routing") connectorAttributes)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `id` -

    Identifier of this charging station. It can only be null when custom
    charging stations from non-HERE datasets have been injected on the
    HERE platform. By default, with HERE datasets it is guranteed to be
    not null.

    `name` -

    Human readable name of this charging station. It can be null when
    there is no name associated with the station.

    `connectorAttributes` -

    Details of the connector suggested to be used.

    </div>

  - <div id="<init>(java.lang.String,java.lang.String,com.here.sdk.routing.ChargingConnectorAttributes,com.here.sdk.core.NameID,com.here.sdk.core.NameID,java.util.List)"
    class="section detail">

    ### ChargingStation

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">ChargingStation</span><span class="parameters">(@Nullable
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> id,
    @Nullable <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> name,
    @Nullable
    [ChargingConnectorAttributes](sdk-for-android-explore-com-here-sdk-routing-chargingconnectorattributes "class in com.here.sdk.routing") connectorAttributes,
    @Nullable
    [NameID](sdk-for-android-explore-com-here-sdk-core-nameid "class in com.here.sdk.core") brand,
    @Nullable
    [NameID](sdk-for-android-explore-com-here-sdk-core-nameid "class in com.here.sdk.core") chargePointOperator,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[NameID](sdk-for-android-explore-com-here-sdk-core-nameid "class in com.here.sdk.core")> matchingEMobilityServiceProviders)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `id` -

    Identifier of this charging station. It can only be null when custom
    charging stations from non-HERE datasets have been injected on the
    HERE platform. By default, with HERE datasets it is guranteed to be
    not null.

    `name` -

    Human readable name of this charging station. It can be null when
    there is no name associated with the station.

    `connectorAttributes` -

    Details of the connector suggested to be used.

    `brand` -

    Charging station brand.
    [`NameID.name`](sdk-for-android-explore-com-here-sdk-core-nameid#name)
    reflect to charging station brand name.
    [`NameID.id`](sdk-for-android-explore-com-here-sdk-core-nameid#id)
    reflect to charging station brand unique ID.

    `chargePointOperator` -

    Charging station charge-point-operator.
    [`NameID.name`](sdk-for-android-explore-com-here-sdk-core-nameid#name)
    reflect to charge-point-operator name.
    [`NameID.id`](sdk-for-android-explore-com-here-sdk-core-nameid#id)
    reflect to charge-point-operator ID.

    `matchingEMobilityServiceProviders` -

    List of matched E-Mobility Service Providers. Populated only when
    [`ElectricVehicleOptions.evMobilityServiceProviderPreferences`](sdk-for-android-explore-com-here-sdk-routing-electricvehicleoptions#evMobilityServiceProviderPreferences)
    was set. This list reflects the subset of E-Mobility Service
    Providers supported by the charging station, from the list specified
    in the request parameter
    [`ElectricVehicleOptions.evMobilityServiceProviderPreferences`](sdk-for-android-explore-com-here-sdk-routing-electricvehicleoptions#evMobilityServiceProviderPreferences).
    [`NameID.name`](sdk-for-android-explore-com-here-sdk-core-nameid#name)
    in each list item reflect to E-Mobility Service Provider name.
    [`NameID.id`](sdk-for-android-explore-com-here-sdk-core-nameid#id)
    in each list item reflect to E-Mobility Service Provider id.

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

