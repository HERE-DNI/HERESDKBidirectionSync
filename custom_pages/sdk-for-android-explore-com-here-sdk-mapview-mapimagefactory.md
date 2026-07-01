---
title: "MapImageFactory (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapimagefactory"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.mapview.MapImageFactory

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public class
</span><span class="element-name type-name-label">MapImageFactory</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Convenience factory class for loading marker resources from various
sources.

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
  href="sdk-for-android-explore-com-here-sdk-mapview-mapimage"
  title="class in com.here.sdk.mapview"><code>MapImage</code></a></td>
  <td><pre><code>fromBitmap(android.graphics.Bitmap bitmap)</code></pre></td>
  <td><div class="block">
  Creates a map image from a supplied Bitmap.
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapimage"
  title="class in com.here.sdk.mapview"><code>MapImage</code></a></td>
  <td><pre><code>fromFile(String filePath,
   int width,
   int height)</code></pre></td>
  <td><div class="block">
  Creates a map image from a specified SVG Tiny or PNG file path.
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapimage"
  title="class in com.here.sdk.mapview"><code>MapImage</code></a></td>
  <td><pre><code>fromResource(android.content.res.Resources resources,
   int resourceID)</code></pre></td>
  <td><div class="block">
  Loads a map image from a specified bitmap resource ID.
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

  - <div id="fromResource(android.content.res.Resources,int)"
    class="section detail">

    ### fromResource

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">[MapImage](sdk-for-android-explore-com-here-sdk-mapview-mapimage "class in com.here.sdk.mapview")</span> <span class="element-name">fromResource</span><span class="parameters">(android.content.res.Resources resources,
    int resourceID)</span>

    </div>

    <div class="block">

    Loads a map image from a specified bitmap resource ID. As usual on
    Android, the PNG format is preferred. Vector drawables are not
    supported.

    </div>

    Parameters:  
    `resources` - the application's resources

    `resourceID` - resource ID for the bitmap image to load

    Returns:  
    map image representing specified image resource

    </div>

  - <div id="fromFile(java.lang.String,int,int)" class="section detail">

    ### fromFile

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">[MapImage](sdk-for-android-explore-com-here-sdk-mapview-mapimage "class in com.here.sdk.mapview")</span> <span class="element-name">fromFile</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> filePath,
    int width, int height)</span> throws
    <span class="exceptions">[InstantiationErrorException](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")</span>

    </div>

    <div class="block">

    Creates a map image from a specified SVG Tiny or PNG file path.
    Trying to load data not compliant to SVG Tiny or PNG might result in
    undefined behavior. This method needs read storage permission to be
    granted.

    </div>

    Parameters:  
    `filePath` - the path pointing to SVG Tiny file

    `width` - preferred width

    `height` - preferred height

    Returns:  
    map image representing specified image resource

    Throws:  
    [`InstantiationErrorException`](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors") -
    if dimension are invalid or path is empty.

    </div>

  - <div id="fromBitmap(android.graphics.Bitmap)"
    class="section detail">

    ### fromBitmap

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">[MapImage](sdk-for-android-explore-com-here-sdk-mapview-mapimage "class in com.here.sdk.mapview")</span> <span class="element-name">fromBitmap</span><span class="parameters">(@NonNull
    android.graphics.Bitmap bitmap)</span>

    </div>

    <div class="block">

    Creates a map image from a supplied Bitmap.

    </div>

    Parameters:  
    `bitmap` - the bitmap image to use for creating the marker resource

    Returns:  
    map image representing specified image resource

    </div>

  </div>

</div>

