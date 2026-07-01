---
title: "TileSource.TileMetadata (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-tilemetadata"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview.datasource](sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.sdk.mapview.datasource.TileSource.TileMetadata

</div>

<div id="class-description" class="section class-description">

Enclosing interface:  
[TileSource](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource "interface in com.here.sdk.mapview.datasource")

<div class="type-signature">

<span class="modifiers">public static final class
</span><span class="element-name type-name-label">TileSource.TileMetadata</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Tile metadata.

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
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html"
  class="external-link"
  title="class or interface in java.util"><code>Date</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-tilemetadata#dataExpiryTimestamp"
  class="member-name-link"><code>dataExpiryTimestamp</code></a></td>
  <td><div class="block">
  Tile data expiry timestamp, relative to Epoch.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-dataversion"
  title="class in com.here.sdk.mapview.datasource"><code>TileSource.DataVersion</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-tilemetadata#dataVersion"
  class="member-name-link"><code>dataVersion</code></a></td>
  <td><div class="block">
  Tile data version.
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
  <td><pre><code>TileMetadata(TileSource.DataVersion dataVersion,
   Date dataExpiryTimestamp)</code></pre></td>
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

  - <div id="dataVersion" class="section detail">

    ### dataVersion

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TileSource.DataVersion](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-dataversion "class in com.here.sdk.mapview.datasource")</span> <span class="element-name">dataVersion</span>

    </div>

    <div class="block">

    Tile data version.

    </div>

    </div>

  - <div id="dataExpiryTimestamp" class="section detail">

    ### dataExpiryTimestamp

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html"
    class="external-link" title="class or interface in java.util">Date</a></span> <span class="element-name">dataExpiryTimestamp</span>

    </div>

    <div class="block">

    Tile data expiry timestamp, relative to Epoch. Sub-second
    time-points are not supported.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(com.here.sdk.mapview.datasource.TileSource.DataVersion,java.util.Date)"
    class="section detail">

    ### TileMetadata

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">TileMetadata</span><span class="parameters">(@NonNull
    [TileSource.DataVersion](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-dataversion "class in com.here.sdk.mapview.datasource") dataVersion,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html"
    class="external-link" title="class or interface in java.util">Date</a> dataExpiryTimestamp)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `dataVersion` -

    Tile data version.

    `dataExpiryTimestamp` -

    Tile data expiry timestamp, relative to Epoch. Sub-second
    time-points are not supported.

    </div>

  </div>

</div>

