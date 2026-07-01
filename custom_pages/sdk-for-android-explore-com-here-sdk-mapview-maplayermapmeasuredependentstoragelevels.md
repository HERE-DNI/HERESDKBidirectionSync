---
title: "MapLayerMapMeasureDependentStorageLevels (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-maplayermapmeasuredependentstoragelevels"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.mapview.MapLayerMapMeasureDependentStorageLevels
→ com.here.NativeBase →
com.here.sdk.mapview.MapLayerMapMeasureDependentStorageLevels

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">MapLayerMapMeasureDependentStorageLevels</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Provides a mapping between a MapLayer map measure to datasource storage
level.

</div>

</div>

<div class="section summary">

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Static Methods
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
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-maplayermapmeasuredependentstoragelevels"
  title="class in com.here.sdk.mapview"><code>MapLayerMapMeasureDependentStorageLevels</code></a></td>
  <td><pre><code>withStorageLevelOffset(int offset)</code></pre></td>
  <td><div class="block">
  Creates an instance of MapLayerMapMeasureDependentStorageLevels with the
  specified storage level offset.
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

  - <div id="withStorageLevelOffset(int)" class="section detail">

    ### withStorageLevelOffset

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[MapLayerMapMeasureDependentStorageLevels](sdk-for-android-explore-com-here-sdk-mapview-maplayermapmeasuredependentstoragelevels "class in com.here.sdk.mapview")</span> <span class="element-name">withStorageLevelOffset</span><span class="parameters">(int offset)</span>

    </div>

    <div class="block">

    Creates an instance of MapLayerMapMeasureDependentStorageLevels with
    the specified storage level offset. This creates a map where the
    storage level is determined by applying an "offset" to the zoom
    level. A negative offset results in a storage level lower than the
    zoom level, while a positive offset increases it. For example, with
    an offset of 0, the storage level matches the zoom level directly.
    An offset of -1 makes the storage level one less than the zoom
    level, and so on. The offset value is clamped to the range of -3
    to 3. Note: The generated mapping adjusts so that when the map
    camera is significantly tilted, the storage level is further reduced
    for data near the horizon.

    </div>

    Parameters:  
    `offset` -

    Defines an offset of storage level from the zoom level. The value
    will be clamped to a range of -3 to 3.

    Returns:  
    MapLayerMapMeasureDependentStorageLevels instance.

    </div>

  </div>

</div>

