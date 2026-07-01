---
title: "AssetsManager (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-assetsmanager"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.NativeBasecom.here.sdk.mapview.AssetsManager
→ com.here.NativeBase → com.here.sdk.mapview.AssetsManager

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">AssetsManager</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Assets manager interface. Can be used to make assets available to the
SDK. Note: This is a beta release of this feature, so there could be a
few bugs and unexpected behavior. Related APIs may change for new
releases without a deprecation process.

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
  <td><pre><code>AssetsManager(MapContext context)</code></pre></td>
  <td><div class="block">
  Creates an instance of AssetsManager.
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
  <td><pre><code>registerFont(String fontName,
   String fontPath)</code></pre></td>
  <td><div class="block">
  Registers a font under a font name.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>registerFontWithFallback(String fontName,
   String fontPath,
   List&lt;String&gt; fallbackFontFilePaths)</code></pre></td>
  <td><div class="block">
  Registers a font set under a font name.
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

  - <div id="<init>(com.here.sdk.mapview.MapContext)"
    class="section detail">

    ### AssetsManager

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">AssetsManager</span><span class="parameters">(@NonNull
    [MapContext](sdk-for-android-explore-com-here-sdk-mapview-mapcontext "class in com.here.sdk.mapview") context)</span>

    </div>

    <div class="block">

    Creates an instance of AssetsManager.

    </div>

    Parameters:  
    `context` -

    MapContext to which the assets belong.

    </div>

  </div>

- <div id="method-detail" class="section method-details">

  - <div id="registerFont(java.lang.String,java.lang.String)"
    class="section detail">

    ### registerFont

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">registerFont</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> fontName,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> fontPath)</span>

    </div>

    <div class="block">

    Registers a font under a font name. After registration, the font
    name can be used in the SVG text tag as font-family attribute
    parameter when creating a MapImage with ImageFormat.SVG .
    MapMarker.TextStyle Repeated registration with the same font name is
    ignored.

    </div>

    Parameters:  
    `fontName` -

    A font name.

    `fontPath` -

    A font file path. TTF, OTF and WOFF formats are supported. Can be an
    asset file path or an absolute file path.

    </div>

  - <div id="registerFontWithFallback(java.lang.String,java.lang.String,java.util.List)"
    class="section detail">

    ### registerFontWithFallback

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">registerFontWithFallback</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> fontName,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> fontPath,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a>> fallbackFontFilePaths)</span>

    </div>

    <div class="block">

    Registers a font set under a font name. After registration, the font
    name can be used in the SVG text tag as font-family attribute
    parameter when creating a MapImage with ImageFormat.SVG .
    MapMarker.TextStyle Repeated registration with the same font name is
    ignored.

    </div>

    Parameters:  
    `fontName` -

    A font name.

    `fontPath` -

    A font file path. TTF, OTF and WOFF formats are supported. Can be an
    asset file path or an absolute file path.

    `fallbackFontFilePaths` -

    Additional font files are intended to be used if main font does not
    contain required character symbol and shall be sorted starting from
    most useful.

    </div>

  </div>

</div>

