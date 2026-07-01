---
title: "TileSource.DataVersion (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-dataversion"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview.datasource](sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.sdk.mapview.datasource.TileSource.DataVersion

</div>

<div id="class-description" class="section class-description">

Enclosing interface:  
[TileSource](sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource "interface in com.here.sdk.mapview.datasource")

<div class="type-signature">

<span class="modifiers">public static final class
</span><span class="element-name type-name-label">TileSource.DataVersion</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Tile data version.

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
  <td><code>int</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-dataversion#majorVersion"
  class="member-name-link"><code>majorVersion</code></a></td>
  <td><div class="block">
  Major version number.
  </div></td>
  </tr>
  <tr>
  <td><code>int</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-dataversion#minorVersion"
  class="member-name-link"><code>minorVersion</code></a></td>
  <td><div class="block">
  Minor version number.
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
  <td><pre><code>DataVersion(int majorVersion,
   int minorVersion)</code></pre></td>
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

  - <div id="majorVersion" class="section detail">

    ### majorVersion

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">majorVersion</span>

    </div>

    <div class="block">

    Major version number. Describes changes in underlying data that
    would require a complete reload (e.g. geometry changes).

    </div>

    </div>

  - <div id="minorVersion" class="section detail">

    ### minorVersion

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">minorVersion</span>

    </div>

    <div class="block">

    Minor version number. Describes changes in underlying data that
    would not require a complete reload (e.g. attributes changes).

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(int,int)" class="section detail">

    ### DataVersion

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">DataVersion</span><span class="parameters">(int majorVersion,
    int minorVersion)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `majorVersion` -

    Major version number. Describes changes in underlying data that
    would require a complete reload (e.g. geometry changes).

    `minorVersion` -

    Minor version number. Describes changes in underlying data that
    would not require a complete reload (e.g. attributes changes).

    </div>

  </div>

</div>

