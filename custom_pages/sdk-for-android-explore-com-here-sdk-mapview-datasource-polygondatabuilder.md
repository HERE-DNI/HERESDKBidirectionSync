---
title: "PolygonDataBuilder (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-polygondatabuilder"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview.datasource](sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.mapview.datasource.PolygonDataBuilder →
com.here.NativeBase → com.here.sdk.mapview.datasource.PolygonDataBuilder

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">PolygonDataBuilder</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Builder of PolygonData instances. The builder can create PolygonData
instances for polygons with an outer boundary and optionally one or more
inner boundaries (holes). Note: This is a beta release of this feature,
so there could be a few bugs and unexpected behavior. Related APIs may
change for new releases without a deprecation process.

</div>

</div>

<div class="section summary">

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
  <td><pre><code>PolygonDataBuilder()</code></pre></td>
  <td><div class="block">
  Creates a builder instance.
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
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-polygondata"
  title="class in com.here.sdk.mapview.datasource"><code>PolygonData</code></a></td>
  <td><pre><code>build()</code></pre></td>
  <td><div class="block">
  Builds an instance of PolygonData and resets the builder instance.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-polygondatabuilder"
  title="class in com.here.sdk.mapview.datasource"><code>PolygonDataBuilder</code></a></td>
  <td><pre><code>withAttributes(DataAttributes attributes)</code></pre></td>
  <td><div class="block">
  Configures the builder with custom attributes for polygon to be created.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-polygondatabuilder"
  title="class in com.here.sdk.mapview.datasource"><code>PolygonDataBuilder</code></a></td>
  <td><pre><code>withGeometry(GeoPolygon geometry)</code></pre></td>
  <td><div class="block">
  Configures the builder with geometry for the polygon to be created.
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

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>()" class="section detail">

    ### PolygonDataBuilder

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">PolygonDataBuilder</span>()

    </div>

    <div class="block">

    Creates a builder instance.

    </div>

    </div>

  </div>

- <div id="method-detail" class="section method-details">

  - <div id="withGeometry(com.here.sdk.core.GeoPolygon)"
    class="section detail">

    ### withGeometry

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[PolygonDataBuilder](sdk-for-android-explore-com-here-sdk-mapview-datasource-polygondatabuilder "class in com.here.sdk.mapview.datasource")</span> <span class="element-name">withGeometry</span><span class="parameters">(@NonNull
    [GeoPolygon](sdk-for-android-explore-com-here-sdk-core-geopolygon "class in com.here.sdk.core") geometry)</span>

    </div>

    <div class="block">

    Configures the builder with geometry for the polygon to be created.

    </div>

    Parameters:  
    `geometry` -

    Geometry of the polygon. The outer boundary has to be ordered
    clockwise and closed. Any inner boundary has to be ordered
    counterclockwise and closed. Altitude of boundary vertices is
    ignored. The visual behaviour for self-intersecting outer boundary
    is undefined.

    Returns:  
    The builder.

    </div>

  - <div id="withAttributes(com.here.sdk.mapview.datasource.DataAttributes)"
    class="section detail">

    ### withAttributes

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[PolygonDataBuilder](sdk-for-android-explore-com-here-sdk-mapview-datasource-polygondatabuilder "class in com.here.sdk.mapview.datasource")</span> <span class="element-name">withAttributes</span><span class="parameters">(@NonNull
    [DataAttributes](sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributes "class in com.here.sdk.mapview.datasource") attributes)</span>

    </div>

    <div class="block">

    Configures the builder with custom attributes for polygon to be
    created.

    </div>

    Parameters:  
    `attributes` -

    Custom data attributes to be associated with the polygon.

    Returns:  
    The builder.

    </div>

  - <div id="build()" class="section detail">

    ### build

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[PolygonData](sdk-for-android-explore-com-here-sdk-mapview-datasource-polygondata "class in com.here.sdk.mapview.datasource")</span> <span class="element-name">build</span>()

    </div>

    <div class="block">

    Builds an instance of PolygonData and resets the builder instance.

    </div>

    Returns:  
    Instance of
    [`PolygonData`](sdk-for-android-explore-com-here-sdk-mapview-datasource-polygondata "class in com.here.sdk.mapview.datasource")
    created with the configured parameters.

    </div>

  </div>

</div>

