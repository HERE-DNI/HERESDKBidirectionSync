---
title: "RouteRailwayCrossing (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-routerailwaycrossing"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.routing.RouteRailwayCrossing

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">RouteRailwayCrossing</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Contains information about railway crossing.

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
  <td><a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates"
  title="class in com.here.sdk.core"><code>GeoCoordinates</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-routerailwaycrossing#coordinates"
  class="member-name-link"><code>coordinates</code></a></td>
  <td><div class="block">
  Location on the route
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-routing-routeoffset"
  title="class in com.here.sdk.routing"><code>RouteOffset</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-routerailwaycrossing#routeOffset"
  class="member-name-link"><code>routeOffset</code></a></td>
  <td><div class="block">
  Route position
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-routerailwaycrossingtype"
  title="enum class in com.here.sdk.routing"><code>RouteRailwayCrossingType</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-routerailwaycrossing#type"
  class="member-name-link"><code>type</code></a></td>
  <td><div class="block">
  The type of the route place.
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
  <td><pre><code>RouteRailwayCrossing(RouteRailwayCrossingType type,
   GeoCoordinates coordinates,
   RouteOffset routeOffset)</code></pre></td>
  <td><div class="block">
  Creates a new instance.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="method-summary" class="section method-summary">

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>`, `<a
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
    </span><span class="modifiers">public</span> <span class="return-type">[RouteRailwayCrossingType](sdk-for-android-explore-com-here-sdk-routing-routerailwaycrossingtype "enum class in com.here.sdk.routing")</span> <span class="element-name">type</span>

    </div>

    <div class="block">

    The type of the route place.

    </div>

    </div>

  - <div id="coordinates" class="section detail">

    ### coordinates

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")</span> <span class="element-name">coordinates</span>

    </div>

    <div class="block">

    Location on the route

    </div>

    </div>

  - <div id="routeOffset" class="section detail">

    ### routeOffset

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[RouteOffset](sdk-for-android-explore-com-here-sdk-routing-routeoffset "class in com.here.sdk.routing")</span> <span class="element-name">routeOffset</span>

    </div>

    <div class="block">

    Route position

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(com.here.sdk.routing.RouteRailwayCrossingType,com.here.sdk.core.GeoCoordinates,com.here.sdk.routing.RouteOffset)"
    class="section detail">

    ### RouteRailwayCrossing

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RouteRailwayCrossing</span><span class="parameters">(@NonNull
    [RouteRailwayCrossingType](sdk-for-android-explore-com-here-sdk-routing-routerailwaycrossingtype "enum class in com.here.sdk.routing") type,
    @NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") coordinates,
    @NonNull
    [RouteOffset](sdk-for-android-explore-com-here-sdk-routing-routeoffset "class in com.here.sdk.routing") routeOffset)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `type` -

    The type of the route place.

    `coordinates` -

    Location on the route

    `routeOffset` -

    Route position

    </div>

  </div>

</div>

