---
title: "EVTruckOptions (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-evtruckoptions"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.routing.EVTruckOptions

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="annotations"><a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html"
class="external-link"
title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public final class
</span><span class="element-name type-name-label">EVTruckOptions</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="deprecation-block">

<span class="deprecated-label">Deprecated.</span>

<div class="deprecation-comment">

Will be removed in v4.28.0. Use `RoutingOptions` class instead.

</div>

</div>

<div class="block">

All the options to specify how a route for an electric truck should be
calculated.

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
  <td><a href="sdk-for-android-explore-com-here-sdk-routing-allowoptions"
  title="class in com.here.sdk.routing"><code>AllowOptions</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-evtruckoptions#allowOptions"
  class="member-name-link"><code>allowOptions</code></a></td>
  <td><div class="block">
  Deprecated.
  </div>
  <div class="block">
  The options explicitly allowed by user for route calculations.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-avoidanceoptions"
  title="class in com.here.sdk.routing"><code>AvoidanceOptions</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-evtruckoptions#avoidanceOptions"
  class="member-name-link"><code>avoidanceOptions</code></a></td>
  <td><div class="block">
  Deprecated.
  </div>
  <div class="block">
  Options to specify restrictions for route calculations.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-transport-truckroadtype"
  title="enum class in com.here.sdk.transport"><code>TruckRoadType</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-evtruckoptions#avoidedTruckRoadTypes"
  class="member-name-link"><code>avoidedTruckRoadTypes</code></a></td>
  <td><div class="block">
  Deprecated.
  </div>
  <div class="block">
  Specifies a list of avoided truck road types for vehicle.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-evconsumptionmodel"
  title="class in com.here.sdk.routing"><code>EVConsumptionModel</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-evtruckoptions#consumptionModel"
  class="member-name-link"><code>consumptionModel</code></a></td>
  <td><div class="block">
  Deprecated.
  </div>
  <div class="block">
  Vehicle specific parameters, which are then used to calculate energy
  consumption for the vehicle on a given route.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-transport-hazardousmaterial"
  title="enum class in com.here.sdk.transport"><code>HazardousMaterial</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-evtruckoptions#hazardousMaterials"
  class="member-name-link"><code>hazardousMaterials</code></a></td>
  <td><div class="block">
  Deprecated.
  </div>
  <div class="block">
  Specifies a list of hazardous materials shipped in the vehicle.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-evtruckoptions#lastCharacterOfLicensePlate"
  class="member-name-link"><code>lastCharacterOfLicensePlate</code></a></td>
  <td><div class="block">
  Deprecated.
  </div>
  <div class="block">
  Specifies the last character of a vehicle's license plate, typically
  used to evaluate traffic restrictions in certain environmental or
  low-emission zones.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-transport-tunnelcategory"
  title="enum class in com.here.sdk.transport"><code>TunnelCategory</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-evtruckoptions#linkTunnelCategory"
  class="member-name-link"><code>linkTunnelCategory</code></a></td>
  <td><div class="block">
  Deprecated.
  </div>
  <div class="block">
  Specifies the tunnel categories to restrict certain route links.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-routing-maxspeedonsegment"
  title="class in com.here.sdk.routing"><code>MaxSpeedOnSegment</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-evtruckoptions#maxSpeedOnSegments"
  class="member-name-link"><code>maxSpeedOnSegments</code></a></td>
  <td><div class="block">
  Deprecated.
  </div>
  <div class="block">
  Segments with restriction on maximum
  DynamicSpeedInfo.baseSpeedInMetersPerSecond .
  </div></td>
  </tr>
  <tr>
  <td><code>int</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-evtruckoptions#occupantsNumber"
  class="member-name-link"><code>occupantsNumber</code></a></td>
  <td><div class="block">
  Deprecated.
  </div>
  <div class="block">
  Specifies the number of occupants in the vehicle, including driver, can
  affect the vehicle's ability to use HOV/carpool restricted lanes.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions"
  title="class in com.here.sdk.routing"><code>RouteOptions</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-evtruckoptions#routeOptions"
  class="member-name-link"><code>routeOptions</code></a></td>
  <td><div class="block">
  Deprecated.
  </div>
  <div class="block">
  Specifies the common route calculation options.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-routetextoptions"
  title="class in com.here.sdk.routing"><code>RouteTextOptions</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-evtruckoptions#textOptions"
  class="member-name-link"><code>textOptions</code></a></td>
  <td><div class="block">
  Deprecated.
  </div>
  <div class="block">
  Customize textual content returned from the route calculation, such as
  localization, format, and unit system.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-routing-tolloptions"
  title="class in com.here.sdk.routing"><code>TollOptions</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-evtruckoptions#tollOptions"
  class="member-name-link"><code>tollOptions</code></a></td>
  <td><div class="block">
  Deprecated.
  </div>
  <div class="block">
  Options to specify how the tolls should be calculated, such as
  transponders, vehicle category, and emission type.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-transport-truckspecifications"
  title="class in com.here.sdk.transport"><code>TruckSpecifications</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-evtruckoptions#truckSpecifications"
  class="member-name-link"><code>truckSpecifications</code></a></td>
  <td><div class="block">
  Deprecated.
  </div>
  <div class="block">
  Detailed truck specifications such as dimensions and weight.
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
  <td><pre><code>EVTruckOptions()</code></pre></td>
  <td><div class="block">
  Deprecated.
  </div>
  <div class="block">
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
  Deprecated Methods

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
  <td><div class="block">
  Deprecated.
  </div>
   </td>
  </tr>
  <tr>
  <td><code>int</code></td>
  <td><pre><code>hashCode()</code></pre></td>
  <td><div class="block">
  Deprecated.
  </div>
   </td>
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

  - <div id="routeOptions" class="section detail">

    ### routeOptions

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[RouteOptions](sdk-for-android-explore-com-here-sdk-routing-routeoptions "class in com.here.sdk.routing")</span> <span class="element-name">routeOptions</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Specifies the common route calculation options.

    </div>

    </div>

  - <div id="textOptions" class="section detail">

    ### textOptions

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[RouteTextOptions](sdk-for-android-explore-com-here-sdk-routing-routetextoptions "class in com.here.sdk.routing")</span> <span class="element-name">textOptions</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Customize textual content returned from the route calculation, such
    as localization, format, and unit system.

    </div>

    </div>

  - <div id="avoidanceOptions" class="section detail">

    ### avoidanceOptions

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[AvoidanceOptions](sdk-for-android-explore-com-here-sdk-routing-avoidanceoptions "class in com.here.sdk.routing")</span> <span class="element-name">avoidanceOptions</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Options to specify restrictions for route calculations. By default
    no restrictions are applied.

    </div>

    </div>

  - <div id="tollOptions" class="section detail">

    ### tollOptions

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TollOptions](sdk-for-android-explore-com-here-sdk-routing-tolloptions "class in com.here.sdk.routing")</span> <span class="element-name">tollOptions</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Options to specify how the tolls should be calculated, such as
    transponders, vehicle category, and emission type.

    </div>

    </div>

  - <div id="allowOptions" class="section detail">

    ### allowOptions

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[AllowOptions](sdk-for-android-explore-com-here-sdk-routing-allowoptions "class in com.here.sdk.routing")</span> <span class="element-name">allowOptions</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    The options explicitly allowed by user for route calculations. By
    default no options are opt in.

    </div>

    </div>

  - <div id="occupantsNumber" class="section detail">

    ### occupantsNumber

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">occupantsNumber</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Specifies the number of occupants in the vehicle, including driver,
    can affect the vehicle's ability to use HOV/carpool restricted
    lanes. Shouldn't be less than 1 or greater than 255. Defaults to 1.
    Note: This parameter has no effect unless HOV and/or HOT lane usage
    is enabled via allowOptions and such lanes are available in the
    selected country.

    </div>

    </div>

  - <div id="lastCharacterOfLicensePlate" class="section detail">

    ### lastCharacterOfLicensePlate

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">lastCharacterOfLicensePlate</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Specifies the last character of a vehicle's license plate, typically
    used to evaluate traffic restrictions in certain environmental or
    low-emission zones. In cities like Bogotá, Mexico City, or Jakarta,
    specific license plate digits may be restricted on certain days or
    in certain areas to reduce congestion and emissions. When this value
    is provided, the HERE SDK considers it during route calculation to
    avoid roads or areas where your vehicle may be restricted based on
    local regulations. Example usage: "7", when the license plate of a
    vehicle looks like "B-ET-182487". If this value is not set, such
    license plate-based restrictions are ignored, and routing is
    performed without considering them.

    </div>

    </div>

  - <div id="maxSpeedOnSegments" class="section detail">

    ### maxSpeedOnSegments

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[MaxSpeedOnSegment](sdk-for-android-explore-com-here-sdk-routing-maxspeedonsegment "class in com.here.sdk.routing")></span> <span class="element-name">maxSpeedOnSegments</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Segments with restriction on maximum
    DynamicSpeedInfo.baseSpeedInMetersPerSecond .

    </div>

    </div>

  - <div id="truckSpecifications" class="section detail">

    ### truckSpecifications

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TruckSpecifications](sdk-for-android-explore-com-here-sdk-transport-truckspecifications "class in com.here.sdk.transport")</span> <span class="element-name">truckSpecifications</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Detailed truck specifications such as dimensions and weight.

    </div>

    </div>

  - <div id="linkTunnelCategory" class="section detail">

    ### linkTunnelCategory

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[TunnelCategory](sdk-for-android-explore-com-here-sdk-transport-tunnelcategory "enum class in com.here.sdk.transport")</span> <span class="element-name">linkTunnelCategory</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Specifies the tunnel categories to restrict certain route links. The
    route will pass only through tunnels of a less strict category.
    Refer to TunnelCategory for the available options.

    </div>

    </div>

  - <div id="hazardousMaterials" class="section detail">

    ### hazardousMaterials

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[HazardousMaterial](sdk-for-android-explore-com-here-sdk-transport-hazardousmaterial "enum class in com.here.sdk.transport")></span> <span class="element-name">hazardousMaterials</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Specifies a list of hazardous materials shipped in the vehicle.
    Refer to HazardousMaterial for the available options.

    </div>

    </div>

  - <div id="avoidedTruckRoadTypes" class="section detail">

    ### avoidedTruckRoadTypes

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[TruckRoadType](sdk-for-android-explore-com-here-sdk-transport-truckroadtype "enum class in com.here.sdk.transport")></span> <span class="element-name">avoidedTruckRoadTypes</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Specifies a list of avoided truck road types for vehicle. Refer to
    TruckRoadType for the available options.

    </div>

    </div>

  - <div id="consumptionModel" class="section detail">

    ### consumptionModel

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[EVConsumptionModel](sdk-for-android-explore-com-here-sdk-routing-evconsumptionmodel "class in com.here.sdk.routing")</span> <span class="element-name">consumptionModel</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Vehicle specific parameters, which are then used to calculate energy
    consumption for the vehicle on a given route.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>()" class="section detail">

    ### EVTruckOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">EVTruckOptions</span>()

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

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

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

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

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

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

