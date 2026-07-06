---
title: "LineDataSourceBuilder (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-linedatasourcebuilder"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview.datasource](sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.mapview.datasource.LineDataSourceBuilder
→ com.here.NativeBase →
com.here.sdk.mapview.datasource.LineDataSourceBuilder

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">LineDataSourceBuilder</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Builder of lines data source. Note: This is a beta release of this
feature, so there could be a few bugs and unexpected behavior. Related
APIs may change for new releases without a deprecation process.

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

      LineDataSourceBuilder(MapContext context)

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

  [`LineDataSource`](sdk-for-android-explore-com-here-sdk-mapview-datasource-linedatasource "class in com.here.sdk.mapview.datasource")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      build()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Builds instance of LineDataSource.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`LineDataSourceBuilder`](sdk-for-android-explore-com-here-sdk-mapview-datasource-linedatasourcebuilder "class in com.here.sdk.mapview.datasource")

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

  [`LineDataSourceBuilder`](sdk-for-android-explore-com-here-sdk-mapview-datasource-linedatasourcebuilder "class in com.here.sdk.mapview.datasource")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      withPolyline(LineData polyline)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Configures the builder to insert the given polyline in the data
  source.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`LineDataSourceBuilder`](sdk-for-android-explore-com-here-sdk-mapview-datasource-linedatasourcebuilder "class in com.here.sdk.mapview.datasource")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      withPolylines(List<LineData> polylines)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Configures the builder to insert the given polylines in the data
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

    ### LineDataSourceBuilder

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">LineDataSourceBuilder</span><span class="parameters">(@NonNull
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
    </span><span class="modifiers">public</span> <span class="return-type">[LineDataSourceBuilder](sdk-for-android-explore-com-here-sdk-mapview-datasource-linedatasourcebuilder "class in com.here.sdk.mapview.datasource")</span> <span class="element-name">withName</span><span class="parameters">(@NonNull
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

  - <div id="sdk-for-android-explore-withPolyline(com.here.sdk.mapview.datasource.LineData)"
    class="section detail">

    ### withPolyline

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[LineDataSourceBuilder](sdk-for-android-explore-com-here-sdk-mapview-datasource-linedatasourcebuilder "class in com.here.sdk.mapview.datasource")</span> <span class="element-name">withPolyline</span><span class="parameters">(@NonNull
    [LineData](sdk-for-android-explore-com-here-sdk-mapview-datasource-linedata "class in com.here.sdk.mapview.datasource") polyline)</span>

    </div>

    <div class="block">

    Configures the builder to insert the given polyline in the data
    source.

    </div>

    Parameters:  
    `polyline` -

    Polyline to add.

    Returns:  
    This data source builder instance.

    </div>

  - <div id="sdk-for-android-explore-withPolylines(java.util.List)"
    class="section detail">

    ### withPolylines

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[LineDataSourceBuilder](sdk-for-android-explore-com-here-sdk-mapview-datasource-linedatasourcebuilder "class in com.here.sdk.mapview.datasource")</span> <span class="element-name">withPolylines</span><span class="parameters">(@NonNull
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[LineData](sdk-for-android-explore-com-here-sdk-mapview-datasource-linedata "class in com.here.sdk.mapview.datasource")\> polylines)</span>

    </div>

    <div class="block">

    Configures the builder to insert the given polylines in the data
    source.

    </div>

    Parameters:  
    `polylines` -

    Polylines to add.

    Returns:  
    This data source builder instance.

    </div>

  - <div id="sdk-for-android-explore-build()" class="section detail">

    ### build

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[LineDataSource](sdk-for-android-explore-com-here-sdk-mapview-datasource-linedatasource "class in com.here.sdk.mapview.datasource")</span> <span class="element-name">build</span>()

    </div>

    <div class="block">

    Builds instance of LineDataSource.

    </div>

    Returns:  
    Instance of the data source created with given polylines and
    attributes.

    </div>

  </div>

</div>

