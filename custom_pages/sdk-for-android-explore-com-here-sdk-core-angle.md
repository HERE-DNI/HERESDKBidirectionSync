---
title: "Angle (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-angle"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core](sdk-for-android-explore-com-here-sdk-core-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.NativeBasecom.here.sdk.core.Angle →
com.here.NativeBase → com.here.sdk.core.Angle

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">Angle</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Represents an angle independent of the unit of measurement.

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
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-core-angle"
  title="class in com.here.sdk.core"><code>Angle</code></a></td>
  <td><pre><code>fromDegrees(double angle)</code></pre></td>
  <td><div class="block">
  Creates a new angle object based on the supplied angle value in degrees.
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-core-angle"
  title="class in com.here.sdk.core"><code>Angle</code></a></td>
  <td><pre><code>fromRadians(double angle)</code></pre></td>
  <td><div class="block">
  Creates a new angle object based on the supplied angle value in radians.
  </div></td>
  </tr>
  <tr>
  <td><code>double</code></td>
  <td><pre><code>getDegrees()</code></pre></td>
  <td><div class="block">
  Gets the value of this angle in degrees.
  </div></td>
  </tr>
  <tr>
  <td><code>double</code></td>
  <td><pre><code>getRadians()</code></pre></td>
  <td><div class="block">
  Gets the value of this angle in radians.
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

  - <div id="fromDegrees(double)" class="section detail">

    ### fromDegrees

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[Angle](sdk-for-android-explore-com-here-sdk-core-angle "class in com.here.sdk.core")</span> <span class="element-name">fromDegrees</span><span class="parameters">(double angle)</span>

    </div>

    <div class="block">

    Creates a new angle object based on the supplied angle value in
    degrees.

    </div>

    Parameters:  
    `angle` -

    Angle value in degrees.

    Returns:  
    The angle as specified by input in degrees.

    </div>

  - <div id="fromRadians(double)" class="section detail">

    ### fromRadians

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[Angle](sdk-for-android-explore-com-here-sdk-core-angle "class in com.here.sdk.core")</span> <span class="element-name">fromRadians</span><span class="parameters">(double angle)</span>

    </div>

    <div class="block">

    Creates a new angle object based on the supplied angle value in
    radians.

    </div>

    Parameters:  
    `angle` -

    Angle value in radians.

    Returns:  
    The angle as specified by input in radians.

    </div>

  - <div id="getDegrees()" class="section detail">

    ### getDegrees

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getDegrees</span>()

    </div>

    <div class="block">

    Gets the value of this angle in degrees.

    </div>

    Returns:  
    The value of this angle in degrees.

    </div>

  - <div id="getRadians()" class="section detail">

    ### getRadians

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getRadians</span>()

    </div>

    <div class="block">

    Gets the value of this angle in radians.

    </div>

    Returns:  
    The value of this angle in radians.

    </div>

  </div>

</div>

