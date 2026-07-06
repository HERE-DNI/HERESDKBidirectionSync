---
title: "PolygonDataSourceBuilder (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-polygondatasourcebuilder"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview.datasource](sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.mapview.datasource.PolygonDataSourceBuilder
→ com.here.NativeBase →
com.here.sdk.mapview.datasource.PolygonDataSourceBuilder

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">PolygonDataSourceBuilder</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Builder of the polygons data source. Note: This is a beta release of
this feature, so there could be a few bugs and unexpected behavior.
Related APIs may change for new releases without a deprecation process.

</div>

</div>

<div class="section summary">

- <div id="sdk-for-android-explore-constructor-summary"
  class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Constructor

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-constructor-name even-row-color">

      PolygonDataSourceBuilder(MapContext context)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a data source builder instance in the given context.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary"
  class="section method-summary">

  <div id="sdk-for-android-explore-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`PolygonDataSource`](sdk-for-android-explore-com-here-sdk-mapview-datasource-polygondatasource "class in com.here.sdk.mapview.datasource")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      build()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Builds a PolygonDataSource instance.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`PolygonDataSourceBuilder`](sdk-for-android-explore-com-here-sdk-mapview-datasource-polygondatasourcebuilder "class in com.here.sdk.mapview.datasource")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      withName(String dataSourceName)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Configures the builder to use the given name for data source.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`PolygonDataSourceBuilder`](sdk-for-android-explore-com-here-sdk-mapview-datasource-polygondatasourcebuilder "class in com.here.sdk.mapview.datasource")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      withPolygon(PolygonData polygon)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Configures the builder to insert the given polygon in the data source.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`PolygonDataSourceBuilder`](sdk-for-android-explore-com-here-sdk-mapview-datasource-polygondatasourcebuilder "class in com.here.sdk.mapview.datasource")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      withPolygons(List<PolygonData> polygon)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Configures the builder to insert the given polygons in the data
  source.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">

  - <div id="sdk-for-android-explore-<init>(com.here.sdk.mapview.MapContext)"
    class="section detail">

    ### PolygonDataSourceBuilder

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">PolygonDataSourceBuilder</span><span class="parameters">(@NonNull
    [MapContext](sdk-for-android-explore-com-here-sdk-mapview-mapcontext "class in com.here.sdk.mapview") context)</span>

    </div>

    <div class="block">

    Creates a data source builder instance in the given context.

    </div>

    Parameters:  
    `context` -

    Map context to associate the data source with.

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-withName(java.lang.String)"
    class="section detail">

    ### withName

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[PolygonDataSourceBuilder](sdk-for-android-explore-com-here-sdk-mapview-datasource-polygondatasourcebuilder "class in com.here.sdk.mapview.datasource")</span> <span class="element-name">withName</span><span class="parameters">(@NonNull
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> dataSourceName)</span>

    </div>

    <div class="block">

    Configures the builder to use the given name for data source.

    </div>

    Parameters:  
    `dataSourceName` -

    Name of the created data source. Must be unique.

    Returns:  
    This data source builder instance.

    </div>

  - <div id="sdk-for-android-explore-withPolygon(com.here.sdk.mapview.datasource.PolygonData)"
    class="section detail">

    ### withPolygon

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[PolygonDataSourceBuilder](sdk-for-android-explore-com-here-sdk-mapview-datasource-polygondatasourcebuilder "class in com.here.sdk.mapview.datasource")</span> <span class="element-name">withPolygon</span><span class="parameters">(@NonNull
    [PolygonData](sdk-for-android-explore-com-here-sdk-mapview-datasource-polygondata "class in com.here.sdk.mapview.datasource") polygon)</span>

    </div>

    <div class="block">

    Configures the builder to insert the given polygon in the data
    source.

    </div>

    Parameters:  
    `polygon` -

    The polygon to add.

    Returns:  
    This data source builder instance.

    </div>

  - <div id="sdk-for-android-explore-withPolygons(java.util.List)"
    class="section detail">

    ### withPolygons

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[PolygonDataSourceBuilder](sdk-for-android-explore-com-here-sdk-mapview-datasource-polygondatasourcebuilder "class in com.here.sdk.mapview.datasource")</span> <span class="element-name">withPolygons</span><span class="parameters">(@NonNull
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[PolygonData](sdk-for-android-explore-com-here-sdk-mapview-datasource-polygondata "class in com.here.sdk.mapview.datasource")\> polygon)</span>

    </div>

    <div class="block">

    Configures the builder to insert the given polygons in the data
    source.

    </div>

    Parameters:  
    `polygon` -

    The polygons to add.

    Returns:  
    This data source builder instance.

    </div>

  - <div id="sdk-for-android-explore-build()" class="section detail">

    ### build

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[PolygonDataSource](sdk-for-android-explore-com-here-sdk-mapview-datasource-polygondatasource "class in com.here.sdk.mapview.datasource")</span> <span class="element-name">build</span>()

    </div>

    <div class="block">

    Builds a PolygonDataSource instance.

    </div>

    Returns:  
    Instance of the data source created with given polygons and
    attributes.

    </div>

  </div>

</div>

