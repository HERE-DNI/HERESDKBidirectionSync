---
title: "PointDataBuilder (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdatabuilder"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview.datasource](sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.mapview.datasource.PointDataBuilder →
com.here.NativeBase → com.here.sdk.mapview.datasource.PointDataBuilder

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">PointDataBuilder</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Builder of PointData instances. Note: This is a beta release of this
feature, so there could be a few bugs and unexpected behavior. Related
APIs may change for new releases without a deprecation process.

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
  <td><pre><code>PointDataBuilder()</code></pre></td>
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
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdata"
  title="class in com.here.sdk.mapview.datasource"><code>PointData</code></a></td>
  <td><pre><code>build()</code></pre></td>
  <td><div class="block">
  Builds an instance of PointData and resets the builder instance.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdatabuilder"
  title="class in com.here.sdk.mapview.datasource"><code>PointDataBuilder</code></a></td>
  <td><pre><code>withAttributes(DataAttributes attributes)</code></pre></td>
  <td><div class="block">
  Configures the builder with custom attributes for point to be created.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdatabuilder"
  title="class in com.here.sdk.mapview.datasource"><code>PointDataBuilder</code></a></td>
  <td><pre><code>withCoordinates(GeoCoordinates coordinates)</code></pre></td>
  <td><div class="block">
  Configures the builder with geodetic coordinates for point to be
  created.
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

    ### PointDataBuilder

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">PointDataBuilder</span>()

    </div>

    <div class="block">

    Creates a builder instance.

    </div>

    </div>

  </div>

- <div id="method-detail" class="section method-details">

  - <div id="withCoordinates(com.here.sdk.core.GeoCoordinates)"
    class="section detail">

    ### withCoordinates

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[PointDataBuilder](sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdatabuilder "class in com.here.sdk.mapview.datasource")</span> <span class="element-name">withCoordinates</span><span class="parameters">(@NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") coordinates)</span>

    </div>

    <div class="block">

    Configures the builder with geodetic coordinates for point to be
    created.

    </div>

    Parameters:  
    `coordinates` -

    Geodetic coordinates of the point. Altitude of coordinates is
    ignored.

    Returns:  
    The builder.

    </div>

  - <div id="withAttributes(com.here.sdk.mapview.datasource.DataAttributes)"
    class="section detail">

    ### withAttributes

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[PointDataBuilder](sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdatabuilder "class in com.here.sdk.mapview.datasource")</span> <span class="element-name">withAttributes</span><span class="parameters">(@NonNull
    [DataAttributes](sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributes "class in com.here.sdk.mapview.datasource") attributes)</span>

    </div>

    <div class="block">

    Configures the builder with custom attributes for point to be
    created.

    </div>

    Parameters:  
    `attributes` -

    Custom data attributes to be associated with the point.

    Returns:  
    The builder.

    </div>

  - <div id="build()" class="section detail">

    ### build

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[PointData](sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdata "class in com.here.sdk.mapview.datasource")</span> <span class="element-name">build</span>()

    </div>

    <div class="block">

    Builds an instance of PointData and resets the builder instance.

    </div>

    Returns:  
    Instance of
    [`PointData`](sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdata "class in com.here.sdk.mapview.datasource")
    created with the configured parameters.

    </div>

  </div>

</div>

