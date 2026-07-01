---
title: "Color (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-color"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core](sdk-for-android-explore-com-here-sdk-core-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.core.Color

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">Color</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Represents a color value. The class is compatible with the native
package android.graphics and replaces native class Color . Usage
example: import com.here.sdk.core.Color; import static
android.graphics.Color.BLUE; import static android.graphics.Color.green;
// Convert native colors to HERE color. Color blue =
Color.valueOf(android.graphics.Color.BLUE); Color anotherColor =
Color.valueOf(0.25f, 0.5f, 0.75f, 0.9f); //ARGB // Retrieve the blue
color component. float blueColorValue = anotherColor.blue(); // = 0.9f
// Convert back to a native color component with the range \[0,255\].
int greenColorValue =
android.graphics.Color.green(anotherColor.toArgb()); // = 230

</div>

</div>

<div class="section summary">

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Static Methods
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
  <td><code>float</code></td>
  <td><pre><code>alpha()</code></pre></td>
  <td> </td>
  </tr>
  <tr>
  <td><code>float</code></td>
  <td><pre><code>blue()</code></pre></td>
  <td> </td>
  </tr>
  <tr>
  <td><code>boolean</code></td>
  <td><pre><code>equals(Object obj)</code></pre></td>
  <td> </td>
  </tr>
  <tr>
  <td><code>float</code></td>
  <td><pre><code>green()</code></pre></td>
  <td> </td>
  </tr>
  <tr>
  <td><code>int</code></td>
  <td><pre><code>hashCode()</code></pre></td>
  <td> </td>
  </tr>
  <tr>
  <td><code>float</code></td>
  <td><pre><code>red()</code></pre></td>
  <td> </td>
  </tr>
  <tr>
  <td><code>int</code></td>
  <td><pre><code>toArgb()</code></pre></td>
  <td><div class="block">
  Converts this color to an ARGB color int.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><pre><code>toString()</code></pre></td>
  <td> </td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-core-color"
  title="class in com.here.sdk.core"><code>Color</code></a></td>
  <td><pre><code>valueOf(float red,
   float green,
   float blue)</code></pre></td>
  <td><div class="block">
  Creates a new opaque color from individual RGB components.
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-core-color"
  title="class in com.here.sdk.core"><code>Color</code></a></td>
  <td><pre><code>valueOf(float red,
   float green,
   float blue,
   float alpha)</code></pre></td>
  <td><div class="block">
  Creates a new color from individual RGBA components.
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-core-color"
  title="class in com.here.sdk.core"><code>Color</code></a></td>
  <td><pre><code>valueOf(int color)</code></pre></td>
  <td> </td>
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
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>`, `<a
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

  - <div id="valueOf(float,float,float)" class="section detail">

    ### valueOf

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[Color](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core")</span> <span class="element-name">valueOf</span><span class="parameters">(float red,
    float green, float blue)</span>

    </div>

    <div class="block">

    Creates a new opaque color from individual RGB components.

    </div>

    Parameters:  
    `red` -

    the value of red component \[0,1\]

    `green` -

    the value of green component \[0,1\]

    `blue` -

    the value of blue component \[0,1\]

    Returns:  
    a new Color instance from given components.

    </div>

  - <div id="valueOf(float,float,float,float)" class="section detail">

    ### valueOf

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[Color](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core")</span> <span class="element-name">valueOf</span><span class="parameters">(float red,
    float green, float blue, float alpha)</span>

    </div>

    <div class="block">

    Creates a new color from individual RGBA components.

    </div>

    Parameters:  
    `red` -

    the value of red component \[0,1\]

    `green` -

    the value of green component \[0,1\]

    `blue` -

    the value of blue component \[0,1\]

    `alpha` -

    the value of alpha component \[0,1\]

    Returns:  
    a new Color instance from given components.

    </div>

  - <div id="valueOf(int)" class="section detail">

    ### valueOf

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[Color](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core")</span> <span class="element-name">valueOf</span><span class="parameters">(@ColorInt
    int color)</span>

    </div>

    Parameters:  
    `color` - ARGB color int

    Returns:  
    a new Color instance from color int.

    </div>

  - <div id="red()" class="section detail">

    ### red

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">float</span> <span class="element-name">red</span>()

    </div>

    Returns:  
    value of red component in range \[0,1\]

    </div>

  - <div id="green()" class="section detail">

    ### green

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">float</span> <span class="element-name">green</span>()

    </div>

    Returns:  
    value of green component in range \[0,1\]

    </div>

  - <div id="blue()" class="section detail">

    ### blue

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">float</span> <span class="element-name">blue</span>()

    </div>

    Returns:  
    value of blue component in range \[0,1\]

    </div>

  - <div id="alpha()" class="section detail">

    ### alpha

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">float</span> <span class="element-name">alpha</span>()

    </div>

    Returns:  
    value of alpha component in range \[0,1\]

    </div>

  - <div id="toArgb()" class="section detail">

    ### toArgb

    <div class="member-signature">

    <span class="annotations">@ColorInt
    </span><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">toArgb</span>()

    </div>

    <div class="block">

    Converts this color to an ARGB color int.

    </div>

    Returns:  
    ARGB color int

    </div>

  - <div id="toString()" class="section detail">

    ### toString

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span>()

    </div>

    Overrides:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()"
    class="external-link"
    title="class or interface in java.lang"><code>toString</code></a> in
    class <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link"
    title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="equals(java.lang.Object)" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><span class="parameters">(<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
    class="external-link"
    title="class or interface in java.lang"><code>equals</code></a> in
    class <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link"
    title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="hashCode()" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
    class="external-link"
    title="class or interface in java.lang"><code>hashCode</code></a> in
    class <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link"
    title="class or interface in java.lang"><code>Object</code></a>

    </div>

  </div>

</div>

