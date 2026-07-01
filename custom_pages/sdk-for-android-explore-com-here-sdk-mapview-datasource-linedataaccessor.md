---
title: "LineDataAccessor (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-linedataaccessor"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview.datasource](sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.mapview.datasource.LineDataAccessor →
com.here.NativeBase → com.here.sdk.mapview.datasource.LineDataAccessor

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">LineDataAccessor</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Line data accessor used for manipulating polylines that are part of a
LineDataSource. Note: This is a beta release of this feature, so there
could be a few bugs and unexpected behavior. Related APIs may change for
new releases without a deprecation process.

</div>

</div>

<div class="section summary">

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
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributesaccessor"
  title="class in com.here.sdk.mapview.datasource"><code>DataAttributesAccessor</code></a></td>
  <td><pre><code>getAttributes()</code></pre></td>
  <td><div class="block">
  Gets polyline attributes accessor.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-geopolyline"
  title="class in com.here.sdk.core"><code>GeoPolyline</code></a></td>
  <td><pre><code>getGeometry()</code></pre></td>
  <td><div class="block">
  Gets polyline geometry.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>setAttributes(DataAttributes attributes)</code></pre></td>
  <td><div class="block">
  Replaces polyline attributes.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>setGeometry(GeoPolyline geometry)</code></pre></td>
  <td><div class="block">
  Replaces polyline geometry.
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

- <div id="method-detail" class="section method-details">

  - <div id="getGeometry()" class="section detail">

    ### getGeometry

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[GeoPolyline](sdk-for-android-explore-com-here-sdk-core-geopolyline "class in com.here.sdk.core")</span> <span class="element-name">getGeometry</span>()

    </div>

    <div class="block">

    Gets polyline geometry.

    </div>

    Returns:  
    The line geometry.

    </div>

  - <div id="getAttributes()" class="section detail">

    ### getAttributes

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[DataAttributesAccessor](sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributesaccessor "class in com.here.sdk.mapview.datasource")</span> <span class="element-name">getAttributes</span>()

    </div>

    <div class="block">

    Gets polyline attributes accessor.

    </div>

    Returns:  
    The polyline attributes accessor.

    </div>

  - <div id="setGeometry(com.here.sdk.core.GeoPolyline)"
    class="section detail">

    ### setGeometry

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setGeometry</span><span class="parameters">(@NonNull
    [GeoPolyline](sdk-for-android-explore-com-here-sdk-core-geopolyline "class in com.here.sdk.core") geometry)</span>

    </div>

    <div class="block">

    Replaces polyline geometry. Altitude of the vertices is ignored.

    </div>

    Parameters:  
    `geometry` -

    The geometry.

    </div>

  - <div id="setAttributes(com.here.sdk.mapview.datasource.DataAttributes)"
    class="section detail">

    ### setAttributes

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAttributes</span><span class="parameters">(@NonNull
    [DataAttributes](sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributes "class in com.here.sdk.mapview.datasource") attributes)</span>

    </div>

    <div class="block">

    Replaces polyline attributes.

    </div>

    Parameters:  
    `attributes` -

    The attributes.

    </div>

  </div>

</div>

