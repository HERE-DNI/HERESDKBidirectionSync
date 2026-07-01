---
title: "AvoidCorridorAreaOptions (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-avoidcorridorareaoptions"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.routing.AvoidCorridorAreaOptions

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">AvoidCorridorAreaOptions</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Area of corridor shape which routes must not cross and exceptions for
this area.

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
  <td><a href="sdk-for-android-explore-com-here-sdk-core-geocorridor"
  title="class in com.here.sdk.core"><code>GeoCorridor</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-avoidcorridorareaoptions#avoidCorridorArea"
  class="member-name-link"><code>avoidCorridorArea</code></a></td>
  <td><div class="block">
  Area of corridor shape which routes must not cross.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-core-geobox"
  title="class in com.here.sdk.core"><code>GeoBox</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-avoidcorridorareaoptions#boundingBoxExceptionAreas"
  class="member-name-link"><code>boundingBoxExceptionAreas</code></a></td>
  <td><div class="block">
  Areas of rectangular shape to exclude from avoidance.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-core-geocorridor"
  title="class in com.here.sdk.core"><code>GeoCorridor</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-avoidcorridorareaoptions#corridorExceptionAreas"
  class="member-name-link"><code>corridorExceptionAreas</code></a></td>
  <td><div class="block">
  Areas of corridor shape to exclude from avoidance.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-core-geopolygon"
  title="class in com.here.sdk.core"><code>GeoPolygon</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-routing-avoidcorridorareaoptions#polygonExceptionAreas"
  class="member-name-link"><code>polygonExceptionAreas</code></a></td>
  <td><div class="block">
  Areas of polygon shape to exclude from avoidance.
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
  <td><pre><code>AvoidCorridorAreaOptions(GeoCorridor avoidCorridorArea)</code></pre></td>
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

  - <div id="avoidCorridorArea" class="section detail">

    ### avoidCorridorArea

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[GeoCorridor](sdk-for-android-explore-com-here-sdk-core-geocorridor "class in com.here.sdk.core")</span> <span class="element-name">avoidCorridorArea</span>

    </div>

    <div class="block">

    Area of corridor shape which routes must not cross. Strictly
    enforced. Violations are reported as
    SectionNoticeCode.VIOLATED_BLOCKED_ROAD . Note: This avoidance
    option is not supported for IsolineOptions . If it is defined for
    isoline calculation then an
    \[sdk.routing.RoutingError.INVALID_PARAMETER\] error is generated.
    Even though GeoCorridor.half_width_in_meters is an optional property
    in case of exception areas it is mandatory. Otherwise route
    calculation will fail with an
    \[sdk.routing.RoutingError.INVALID_PARAMETER\] error.

    </div>

    </div>

  - <div id="boundingBoxExceptionAreas" class="section detail">

    ### boundingBoxExceptionAreas

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[GeoBox](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core")></span> <span class="element-name">boundingBoxExceptionAreas</span>

    </div>

    <div class="block">

    Areas of rectangular shape to exclude from avoidance.

    </div>

    </div>

  - <div id="polygonExceptionAreas" class="section detail">

    ### polygonExceptionAreas

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[GeoPolygon](sdk-for-android-explore-com-here-sdk-core-geopolygon "class in com.here.sdk.core")></span> <span class="element-name">polygonExceptionAreas</span>

    </div>

    <div class="block">

    Areas of polygon shape to exclude from avoidance.

    </div>

    </div>

  - <div id="corridorExceptionAreas" class="section detail">

    ### corridorExceptionAreas

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[GeoCorridor](sdk-for-android-explore-com-here-sdk-core-geocorridor "class in com.here.sdk.core")></span> <span class="element-name">corridorExceptionAreas</span>

    </div>

    <div class="block">

    Areas of corridor shape to exclude from avoidance. Note: Even though
    GeoCorridor.half_width_in_meters is an optional property in case of
    exception areas it is mandatory. Otherwise route calculation will
    fail with an \[sdk.routing.RoutingError.INVALID_PARAMETER\] error.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(com.here.sdk.core.GeoCorridor)"
    class="section detail">

    ### AvoidCorridorAreaOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">AvoidCorridorAreaOptions</span><span class="parameters">(@NonNull
    [GeoCorridor](sdk-for-android-explore-com-here-sdk-core-geocorridor "class in com.here.sdk.core") avoidCorridorArea)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `avoidCorridorArea` -

    Area of corridor shape which routes must not cross. Strictly
    enforced. Violations are reported as
    [`SectionNoticeCode.VIOLATED_BLOCKED_ROAD`](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#VIOLATED_BLOCKED_ROAD).
    **Note:** This avoidance option is not supported for
    `IsolineOptions`. If it is defined for isoline calculation then an
    \[sdk.routing.RoutingError.INVALID_PARAMETER\] error is generated.
    Even though `GeoCorridor.half_width_in_meters` is an optional
    property in case of exception areas it is mandatory. Otherwise route
    calculation will fail with an
    \[sdk.routing.RoutingError.INVALID_PARAMETER\] error.

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

