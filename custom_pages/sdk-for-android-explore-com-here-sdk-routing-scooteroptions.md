---
title: "ScooterOptions (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-scooteroptions"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.routing.ScooterOptions

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="annotations"><a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html"
class="external-link"
title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public final class
</span><span class="element-name type-name-label">ScooterOptions</span>
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

All the options to specify how a scooter route should be calculated.

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
  <td><code>boolean</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-scooteroptions#allowHighway"
  class="member-name-link"><code>allowHighway</code></a></td>
  <td><div class="block">
  Deprecated.
  </div>
  <div class="block">
  Specifies whether scooter is allowed on highway or not.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-avoidanceoptions"
  title="class in com.here.sdk.routing"><code>AvoidanceOptions</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-scooteroptions#avoidanceOptions"
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
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-scooteroptions#engineSizeInCubicCentimeters"
  class="member-name-link"><code>engineSizeInCubicCentimeters</code></a></td>
  <td><div class="block">
  Deprecated.
  </div>
  <div class="block">
  Engine size of the scooter in cubic centimeters.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-scooteroptions#lastCharacterOfLicensePlate"
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
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-routing-maxspeedonsegment"
  title="class in com.here.sdk.routing"><code>MaxSpeedOnSegment</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-scooteroptions#maxSpeedOnSegments"
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
  href="sdk-for-android-explore-com-here-sdk-routing-scooteroptions#occupantsNumber"
  class="member-name-link"><code>occupantsNumber</code></a></td>
  <td><div class="block">
  Deprecated.
  </div>
  <div class="block">
  Specifies the number of occupants in the vehicle, including driver.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions"
  title="class in com.here.sdk.routing"><code>RouteOptions</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-scooteroptions#routeOptions"
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
  href="sdk-for-android-explore-com-here-sdk-routing-scooteroptions#textOptions"
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
  href="sdk-for-android-explore-com-here-sdk-routing-scooteroptions#tollOptions"
  class="member-name-link"><code>tollOptions</code></a></td>
  <td><div class="block">
  Deprecated.
  </div>
  <div class="block">
  Options to specify how the tolls should be calculated, such as
  transponders, vehicle category, and emission type.
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
  <td><pre><code>ScooterOptions()</code></pre></td>
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

  - <div id="occupantsNumber" class="section detail">

    ### occupantsNumber

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">occupantsNumber</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Specifies the number of occupants in the vehicle, including driver.
    Shouldn't be less than 1 or greater than 255. Defaults to 1. This
    option is only relevant for Japan and will be ignored for other
    countries.

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

  - <div id="allowHighway" class="section detail">

    ### allowHighway

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">allowHighway</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Specifies whether scooter is allowed on highway or not. True means
    scooter is allowed to use highways and false means otherwise. By
    default it is set to false . Note that there is a similar parameter
    in AvoidanceOptions , to disallow highway usage, see
    RoadFeatures.CONTROLLED_ACCESS_HIGHWAY . As the avoidance options
    takes precedence, if this parameter is also used, then scooters are
    not allowed to use highways even if allowHighway is set to true .
    However, if no alternative route is possible, the calculated route
    may use highways. In such a case, a SectionNotice will be provided
    in the related Section to indicate that the highway usage
    restriction is violated on this route. A few examples: 1 - If no
    avoidance option is set, and allowHighway = false , when no route is
    found without highway usage, a notice is received. 2 - If no
    avoidance option is set, and allowHighway = true , when no route is
    found without highway usage, no notice is received. 3 - If only
    avoid\[features\] = controlledAccessHighway is set, when no route is
    found without highway usage, a notice is received. 4 - If both
    avoid\[features\] = controlledAccessHighway and allowHighway = true
    are set, when no route is found without highway usage, a notice is
    received.

    </div>

    </div>

  - <div id="engineSizeInCubicCentimeters" class="section detail">

    ### engineSizeInCubicCentimeters

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">engineSizeInCubicCentimeters</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Engine size of the scooter in cubic centimeters. Shouldn't be less
    than 1 or greater than 65535. Default value is null , which means
    the scooter route calculation ignores all engine size limits on the
    road. Note: For now, this option is only relevant in Japan and will
    be ignored for other countries. Currently, map data for this option
    is only available for Japan.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>()" class="section detail">

    ### ScooterOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">ScooterOptions</span>()

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

