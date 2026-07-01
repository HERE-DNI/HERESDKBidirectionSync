---
title: "PolygonDataSource (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-polygondatasource"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview.datasource](sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.mapview.datasource.PolygonDataSource →
com.here.NativeBase → com.here.sdk.mapview.datasource.PolygonDataSource

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">PolygonDataSource</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Polygon data source allows the rendering engine access to the user
provided polygons geometry and their attributes. Polygon segments are
rendered following the shortest path between their end points. Note:
This is a beta release of this feature, so there could be a few bugs and
unexpected behavior. Related APIs may change for new releases without a
deprecation process.

</div>

</div>

<div class="section summary">

- <div id="nested-class-summary" class="section nested-class-summary">

  <div class="caption">

  Nested Classes

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
  <th>Class</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>static interface </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-polygondatasource-polygondataprocessor"
  class="type-name-link"
  title="interface in com.here.sdk.mapview.datasource"><code>PolygonDataSource.PolygonDataProcessor</code></a></td>
  <td><div class="block">
  Called for each polygon, allowing inspection, removal or update of
  coordinates and attributes.
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
  <td><code>void</code></td>
  <td><pre><code>add(PolygonData polygon)</code></pre></td>
  <td><div class="block">
  Adds a new polygon to the data source.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>add(List&lt;PolygonData&gt; polygons)</code></pre></td>
  <td><div class="block">
  Adds new polygons to the data source.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>destroy()</code></pre></td>
  <td><div class="block">
  Frees all internally used resources.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>forEach(PolygonDataSource.PolygonDataProcessor processor)</code></pre></td>
  <td><div class="block">
  Iterates through all the polygons from the data source and passes them
  to the given processor, one by one.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>removeAll()</code></pre></td>
  <td><div class="block">
  Removes all polygons from the data source.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>removeIf(PolygonDataSource.PolygonDataProcessor inspector)</code></pre></td>
  <td><div class="block">
  Iterates through all the polygons from the data source and passes them
  to the given inspector, one by one.
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

  - <div id="add(com.here.sdk.mapview.datasource.PolygonData)"
    class="section detail">

    ### add

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">add</span><span class="parameters">(@NonNull
    [PolygonData](sdk-for-android-explore-com-here-sdk-mapview-datasource-polygondata "class in com.here.sdk.mapview.datasource") polygon)</span>

    </div>

    <div class="block">

    Adds a new polygon to the data source.

    </div>

    Parameters:  
    `polygon` -

    Polygon to add.

    </div>

  - <div id="add(java.util.List)" class="section detail">

    ### add

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">add</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[PolygonData](sdk-for-android-explore-com-here-sdk-mapview-datasource-polygondata "class in com.here.sdk.mapview.datasource")> polygons)</span>

    </div>

    <div class="block">

    Adds new polygons to the data source.

    </div>

    Parameters:  
    `polygons` -

    Polygons to add.

    </div>

  - <div id="removeAll()" class="section detail">

    ### removeAll

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeAll</span>()

    </div>

    <div class="block">

    Removes all polygons from the data source.

    </div>

    </div>

  - <div id="forEach(com.here.sdk.mapview.datasource.PolygonDataSource.PolygonDataProcessor)"
    class="section detail">

    ### forEach

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">forEach</span><span class="parameters">(@NonNull
    [PolygonDataSource.PolygonDataProcessor](sdk-for-android-explore-com-here-sdk-mapview-datasource-polygondatasource-polygondataprocessor "interface in com.here.sdk.mapview.datasource") processor)</span>

    </div>

    <div class="block">

    Iterates through all the polygons from the data source and passes
    them to the given processor, one by one. The processor can update
    the polygon data. The iteration stops after all polygons have been
    processed or the processor returns false from the process call.

    </div>

    Parameters:  
    `processor` -

    Polygon processor.

    </div>

  - <div id="removeIf(com.here.sdk.mapview.datasource.PolygonDataSource.PolygonDataProcessor)"
    class="section detail">

    ### removeIf

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeIf</span><span class="parameters">(@NonNull
    [PolygonDataSource.PolygonDataProcessor](sdk-for-android-explore-com-here-sdk-mapview-datasource-polygondatasource-polygondataprocessor "interface in com.here.sdk.mapview.datasource") inspector)</span>

    </div>

    <div class="block">

    Iterates through all the polygons from the data source and passes
    them to the given inspector, one by one. All polygons for which the
    inspector returns true get removed from the data source. The
    inspector cannot update the polygon data.

    </div>

    Parameters:  
    `inspector` -

    Polygon data processor.

    </div>

  - <div id="destroy()" class="section detail">

    ### destroy

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">destroy</span>()

    </div>

    <div class="block">

    Frees all internally used resources. After calling this method, the
    object is not usable anymore.

    </div>

    </div>

  </div>

</div>

