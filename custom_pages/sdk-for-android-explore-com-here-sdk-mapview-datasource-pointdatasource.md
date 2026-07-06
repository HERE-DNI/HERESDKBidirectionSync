---
title: "PointDataSource (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdatasource"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview.datasource](sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.mapview.datasource.PointDataSource →
com.here.NativeBase → com.here.sdk.mapview.datasource.PointDataSource

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">PointDataSource</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Point data source allows the rendering engine access to the user
provided geographical locations and their attributes. Note: This is a
beta release of this feature, so there could be a few bugs and
unexpected behavior. Related APIs may change for new releases without a
deprecation process.

</div>

</div>

<div class="section summary">

- <div id="sdk-for-android-explore-nested-class-summary"
  class="section nested-class-summary">

  <div class="caption">

  Nested Classes

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Class

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  `static interface `

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdatasource-pointdataprocessor"
  class="type-name-link"
  title="interface in com.here.sdk.mapview.datasource"><code>PointDataSource.PointDataProcessor</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Called for each point, allowing inspection, removal or update of
  coordinates and attributes.

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

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      add(PointData point)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Adds a new point to the data source.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      add(List<PointData> points)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Adds new points to the data source.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      destroy()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Frees all internally used resources.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      forEach(PointDataSource.PointDataProcessor processor)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Iterates through all the points from the data source and passes them
  to the given processor, one by one.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      removeAll()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Removes all points from the data source.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      removeIf(PointDataSource.PointDataProcessor processor)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Iterates through all the points from the data source and passes them
  to the given inspector, one by one.

  </div>

  </div>

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

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-add(com.here.sdk.mapview.datasource.PointData)"
    class="section detail">

    ### add

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">add</span><span class="parameters">(@NonNull
    [PointData](sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdata "class in com.here.sdk.mapview.datasource") point)</span>

    </div>

    <div class="block">

    Adds a new point to the data source. Altitude of the point
    coordinates is ignored.

    </div>

    Parameters:  
    `point` -

    Point to be added.

    </div>

  - <div id="sdk-for-android-explore-add(java.util.List)"
    class="section detail">

    ### add

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">add</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[PointData](sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdata "class in com.here.sdk.mapview.datasource")\> points)</span>

    </div>

    <div class="block">

    Adds new points to the data source. Altitude of the points
    coordinates is ignored.

    </div>

    Parameters:  
    `points` -

    Point positions.

    </div>

  - <div id="sdk-for-android-explore-removeAll()"
    class="section detail">

    ### removeAll

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeAll</span>()

    </div>

    <div class="block">

    Removes all points from the data source.

    </div>

    </div>

  - <div id="sdk-for-android-explore-forEach(com.here.sdk.mapview.datasource.PointDataSource.PointDataProcessor)"
    class="section detail">

    ### forEach

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">forEach</span><span class="parameters">(@NonNull
    [PointDataSource.PointDataProcessor](sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdatasource-pointdataprocessor "interface in com.here.sdk.mapview.datasource") processor)</span>

    </div>

    <div class="block">

    Iterates through all the points from the data source and passes them
    to the given processor, one by one. The processor can update the
    point data. The iteration stops after all points have been processed
    or the processor returns false from the process call.

    </div>

    Parameters:  
    `processor` -

    Point data processor.

    </div>

  - <div id="sdk-for-android-explore-removeIf(com.here.sdk.mapview.datasource.PointDataSource.PointDataProcessor)"
    class="section detail">

    ### removeIf

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeIf</span><span class="parameters">(@NonNull
    [PointDataSource.PointDataProcessor](sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdatasource-pointdataprocessor "interface in com.here.sdk.mapview.datasource") processor)</span>

    </div>

    <div class="block">

    Iterates through all the points from the data source and passes them
    to the given inspector, one by one. All points for which the
    inspector returns true get removed from the data source. The
    inspector cannot update the point data.

    </div>

    Parameters:  
    `processor` -

    Point data processor.

    </div>

  - <div id="sdk-for-android-explore-destroy()" class="section detail">

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

