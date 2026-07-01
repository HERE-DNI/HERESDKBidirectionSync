---
title: "RoutePlace (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-routeplace"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.routing.RoutePlace

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">RoutePlace</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

The location information.

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
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-routeplace#chargeInKilowattHours"
  class="member-name-link"><code>chargeInKilowattHours</code></a></td>
  <td><div class="block">
  Estimated battery charge in kWh for electric vehicles when leaving this
  place.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-chargingstation"
  title="class in com.here.sdk.routing"><code>ChargingStation</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-routeplace#chargingStation"
  class="member-name-link"><code>chargingStation</code></a></td>
  <td><div class="block">
  Charging station data for electric vehicles.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates"
  title="class in com.here.sdk.core"><code>GeoCoordinates</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-routeplace#displayCoordinates"
  class="member-name-link"><code>displayCoordinates</code></a></td>
  <td><div class="block">
  Location of the Points of Interest (PoI) to be displayed in the
  visualization.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a href="sdk-for-android-explore-com-here-sdk-routing-routeplace#id"
  class="member-name-link"><code>id</code></a></td>
  <td><div class="block">
  Identifier of a public transit place if available.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates"
  title="class in com.here.sdk.core"><code>GeoCoordinates</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-routeplace#mapMatchedCoordinates"
  class="member-name-link"><code>mapMatchedCoordinates</code></a></td>
  <td><div class="block">
  Map-matched geographic coordinates.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-routeplace#name"
  class="member-name-link"><code>name</code></a></td>
  <td><div class="block">
  Name of a public transit place if available.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates"
  title="class in com.here.sdk.core"><code>GeoCoordinates</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-routeplace#originalCoordinates"
  class="member-name-link"><code>originalCoordinates</code></a></td>
  <td><div class="block">
  User-defined geographic coordinates.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-routeplace#platform"
  class="member-name-link"><code>platform</code></a></td>
  <td><div class="block">
  Platform name or number of a public transit place if available.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-sideofdestination"
  title="enum class in com.here.sdk.routing"><code>SideOfDestination</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-routeplace#sideOfDestination"
  class="member-name-link"><code>sideOfDestination</code></a></td>
  <td><div class="block">
  Side of destination: left, right or undefined.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-routeplacetype"
  title="enum class in com.here.sdk.routing"><code>RoutePlaceType</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-routeplace#type"
  class="member-name-link"><code>type</code></a></td>
  <td><div class="block">
  The type of the route place.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-routeplace#waypointIndex"
  class="member-name-link"><code>waypointIndex</code></a></td>
  <td><div class="block">
  If available, this index corresponds to the waypoint in the original
  user-defined waypoint list.
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
  <td><pre><code>RoutePlace(RoutePlaceType type,
   GeoCoordinates mapMatchedCoordinates)</code></pre></td>
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
  <tr>
  <td><code>boolean</code></td>
  <td><pre><code>isOffRoad()</code></pre></td>
  <td><div class="block">
  Checks whether the RoutePlace is off-road or not.
  </div></td>
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

  - <div id="type" class="section detail">

    ### type

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[RoutePlaceType](sdk-for-android-explore-com-here-sdk-routing-routeplacetype "enum class in com.here.sdk.routing")</span> <span class="element-name">type</span>

    </div>

    <div class="block">

    The type of the route place.

    </div>

    </div>

  - <div id="waypointIndex" class="section detail">

    ### waypointIndex

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">waypointIndex</span>

    </div>

    <div class="block">

    If available, this index corresponds to the waypoint in the original
    user-defined waypoint list. Otherwise, this waypoint was added
    during route calculation by the system.

    </div>

    </div>

  - <div id="originalCoordinates" class="section detail">

    ### originalCoordinates

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")</span> <span class="element-name">originalCoordinates</span>

    </div>

    <div class="block">

    User-defined geographic coordinates. If not available, it means this
    place was added during route calculation.

    </div>

    </div>

  - <div id="mapMatchedCoordinates" class="section detail">

    ### mapMatchedCoordinates

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")</span> <span class="element-name">mapMatchedCoordinates</span>

    </div>

    <div class="block">

    Map-matched geographic coordinates.

    </div>

    </div>

  - <div id="displayCoordinates" class="section detail">

    ### displayCoordinates

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")</span> <span class="element-name">displayCoordinates</span>

    </div>

    <div class="block">

    Location of the Points of Interest (PoI) to be displayed in the
    visualization. In the map data, PoI have a set of display
    coordinates as well as a set of access/routing coordinates. While
    the access/routing coordinates specify the nearest accessible road
    network location that can be apart from actual location of the PoI,
    the display coordinates specify the location of the PoI to be
    displayed accurately in the visualization.

    </div>

    </div>

  - <div id="chargeInKilowattHours" class="section detail">

    ### chargeInKilowattHours

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">chargeInKilowattHours</span>

    </div>

    <div class="block">

    Estimated battery charge in kWh for electric vehicles when leaving
    this place. Available only if the route was calculated with
    ElectricVehicleOptions.ensureReachability = true .

    </div>

    </div>

  - <div id="chargingStation" class="section detail">

    ### chargingStation

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[ChargingStation](sdk-for-android-explore-com-here-sdk-routing-chargingstation "class in com.here.sdk.routing")</span> <span class="element-name">chargingStation</span>

    </div>

    <div class="block">

    Charging station data for electric vehicles.

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

    Name of a public transit place if available.

    </div>

    </div>

  - <div id="id" class="section detail">

    ### id

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">id</span>

    </div>

    <div class="block">

    Identifier of a public transit place if available.

    </div>

    </div>

  - <div id="platform" class="section detail">

    ### platform

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">platform</span>

    </div>

    <div class="block">

    Platform name or number of a public transit place if available.

    </div>

    </div>

  - <div id="sideOfDestination" class="section detail">

    ### sideOfDestination

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[SideOfDestination](sdk-for-android-explore-com-here-sdk-routing-sideofdestination "enum class in com.here.sdk.routing")</span> <span class="element-name">sideOfDestination</span>

    </div>

    <div class="block">

    Side of destination: left, right or undefined. null for transit
    sections and for origin points. UNDEFINED if originalCoordinates are
    not identified or too close to the road.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(com.here.sdk.routing.RoutePlaceType,com.here.sdk.core.GeoCoordinates)"
    class="section detail">

    ### RoutePlace

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RoutePlace</span><span class="parameters">(@NonNull
    [RoutePlaceType](sdk-for-android-explore-com-here-sdk-routing-routeplacetype "enum class in com.here.sdk.routing") type,
    @NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") mapMatchedCoordinates)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `type` -

    The type of the route place.

    `mapMatchedCoordinates` -

    Map-matched geographic coordinates.

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

  - <div id="isOffRoad()" class="section detail">

    ### isOffRoad

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isOffRoad</span>()

    </div>

    <div class="block">

    Checks whether the RoutePlace is off-road or not.

    </div>

    Returns:  
    `true` if the
    [`RoutePlace`](sdk-for-android-explore-com-here-sdk-routing-routeplace "class in com.here.sdk.routing")
    is off-road, `false` otherwise.

    </div>

  </div>

</div>

