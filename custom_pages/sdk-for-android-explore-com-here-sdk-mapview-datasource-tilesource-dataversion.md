---
title: "TileSource.DataVersion (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-dataversion"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary">com.here.sdk.mapview.datasource</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.mapview.datasource.TileSource.DataVersion → com.here.sdk.mapview.datasource.TileSource.DataVersion

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

Enclosing interface:  
<a href="sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource" title="interface in com.here.sdk.mapview.datasource">TileSource</a>

<div class="type-signature">

<span class="modifiers">public static final class </span><span class="element-name type-name-label">TileSource.DataVersion</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Tile data version.

</div>

</div>

- <div id="sdk-for-android-explore-field-summary" class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Field

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  `int`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-dataversion#majorVersion" class="member-name-link"><code>majorVersion</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Major version number.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `int`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-datasource-tilesource-dataversion#minorVersion" class="member-name-link"><code>minorVersion</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Minor version number.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-constructor-summary" class="section constructor-summary">

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

      DataVersion (int majorVersion,
       int minorVersion)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary" class="section method-summary">

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-field-detail" class="section field-details">

  - <div id="sdk-for-android-explore-majorVersion" class="section detail">

    ### majorVersion

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">majorVersion</span>

    </div>

    <div class="block">

    Major version number. Describes changes in underlying data that would require a complete reload (e.g. geometry changes).

    </div>

    </div>

  - <div id="sdk-for-android-explore-minorVersion" class="section detail">

    ### minorVersion

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">minorVersion</span>

    </div>

    <div class="block">

    Minor version number. Describes changes in underlying data that would not require a complete reload (e.g. attributes changes).

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-explore-init-int-int" class="section detail">

    ### DataVersion

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">DataVersion</span><wbr></wbr><span class="parameters">(int majorVersion, int minorVersion)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `majorVersion` -

    Major version number. Describes changes in underlying data that would require a complete reload (e.g. geometry changes).

    `minorVersion` -

    Minor version number. Describes changes in underlying data that would not require a complete reload (e.g. attributes changes).

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

