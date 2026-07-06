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

<div id="sdk-for-android-explore-class-description"
class="section class-description">

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
<div id="sdk-for-android-explore-method-summary"
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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `[`Angle`](sdk-for-android-explore-com-here-sdk-core-angle "class in com.here.sdk.core")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      fromDegrees(double angle)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Creates a new angle object based on the supplied angle value in
  degrees.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `[`Angle`](sdk-for-android-explore-com-here-sdk-core-angle "class in com.here.sdk.core")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      fromRadians(double angle)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Creates a new angle object based on the supplied angle value in
  radians.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `double`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getDegrees()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the value of this angle in degrees.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `double`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getRadians()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the value of this angle in radians.

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
<div id="sdk-for-android-explore-method-detail"
  class="section method-details">
<div id="sdk-for-android-explore-fromDegrees(double)"
    class="section detail">

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
<div id="sdk-for-android-explore-fromRadians(double)"
    class="section detail">

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
<div id="sdk-for-android-explore-getDegrees()"
    class="section detail">

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
<div id="sdk-for-android-explore-getRadians()"
    class="section detail">

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

