---
title: "AngleRange (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-anglerange"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core](sdk-for-android-explore-com-here-sdk-core-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.core.AngleRange → com.here.sdk.core.AngleRange

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">AngleRange</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Represents angle ranges as a circular sector by using an absolute start angle and a relative range angle called extent. They both define a sector on a circle. All angles are in degrees and are clockwise-oriented. By default, the AngleRange represents the entire circle, the value is in the range of \[0, 360\]. Values will be corrected during construction using normalization for the start angle and clamping for the extent angle, ensuring a valid range for all possible inputs.

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

  `final double`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-core-anglerange#extent" class="member-name-link"><code>extent</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The angle range extent, running clockwise, in degrees from start.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `final double`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-core-anglerange#start" class="member-name-link"><code>start</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Start angle, running clockwise, in degrees from north.

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

      AngleRange ()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Constructs a range covering a full circle.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      AngleRange (double start,
       double extent)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Constructs an AngleRange from the provided start and extent angles.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary" class="section method-summary">

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

  `double`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      closestInRange (double angleClockwiseInDegreesFromNorth)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Get the angle that is closest to the given one and in range.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      equals ( Object obj)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `[`AngleRange`](sdk-for-android-explore-com-here-sdk-core-anglerange "class in com.here.sdk.core")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      fromDirectionDegreesClockwise (double center,
       double extent)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Constructs an AngleRange from the provided center angle defining the direction and an angular width to extent the range by 50% clockwise and 50% counter-clockwise from its center angle.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `[`AngleRange`](sdk-for-android-explore-com-here-sdk-core-anglerange "class in com.here.sdk.core")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      fromMinMaxDegreesClockwise (double min,
       double max)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Constructs an AngleRange from the provided minimum and maximum angles.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      inRange (double angleClockwiseInDegreesFromNorth)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Check if a given angle in degrees, clockwise from north is in range or not.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `double`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      max ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Get the maximum angle defined by the range in degrees, clockwise from north, normalized to \[0,360).

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-field-detail" class="section field-details">

  - <div id="sdk-for-android-explore-start" class="section detail">

    ### start

    <div class="member-signature">

    <span class="modifiers">public final</span> <span class="return-type">double</span> <span class="element-name">start</span>

    </div>

    <div class="block">

    Start angle, running clockwise, in degrees from north. The value is in the range of \[0, 360) degrees.

    </div>

    </div>

  - <div id="sdk-for-android-explore-extent" class="section detail">

    ### extent

    <div class="member-signature">

    <span class="modifiers">public final</span> <span class="return-type">double</span> <span class="element-name">extent</span>

    </div>

    <div class="block">

    The angle range extent, running clockwise, in degrees from start. The value is in the range of \[0, 360\] degrees.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-explore-init-double-double" class="section detail">

    ### AngleRange

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">AngleRange</span><wbr></wbr><span class="parameters">(double start, double extent)</span>

    </div>

    <div class="block">

    Constructs an AngleRange from the provided start and extent angles. Corrects values if they exceed the ranges.

    </div>

    Parameters:  
    `start` -

    Start angle, running clockwise, in degrees from north. The value will be normalized to \[0.0, 360.0).

    `extent` -

    The range's extent, running clockwise, in degrees from start. The value will be clamped to the range of \[0, 360\] degrees.

    </div>

  - <div id="sdk-for-android-explore-init" class="section detail">

    ### AngleRange

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">AngleRange</span>()

    </div>

    <div class="block">

    Constructs a range covering a full circle.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-equals-java-lang-Object" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-explore-hashCode" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-explore-fromMinMaxDegreesClockwise-double-double" class="section detail">

    ### fromMinMaxDegreesClockwise

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public static</span> <span class="return-type">[AngleRange](sdk-for-android-explore-com-here-sdk-core-anglerange "class in com.here.sdk.core")</span> <span class="element-name">fromMinMaxDegreesClockwise</span><wbr></wbr><span class="parameters">(double min, double max)</span>

    </div>

    <div class="block">

    Constructs an AngleRange from the provided minimum and maximum angles. Corrects values if they exceed the ranges. The angles are always interpreted in clockwise orientation.

    </div>

    Parameters:  
    `min` -

    Angle where to start the circular sector, running clockwise, in degrees from north. The value will be normalized to \[0.0, 360.0).

    `max` -

    Angle where the circular sector ends, running clockwise, in degrees from north. The value will be normalized to \[0.0, 360.0).

    Returns:  
    Created AngleRange from the provided minimum and maximum angles.

    </div>

  - <div id="sdk-for-android-explore-fromDirectionDegreesClockwise-double-double" class="section detail">

    ### fromDirectionDegreesClockwise

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public static</span> <span class="return-type">[AngleRange](sdk-for-android-explore-com-here-sdk-core-anglerange "class in com.here.sdk.core")</span> <span class="element-name">fromDirectionDegreesClockwise</span><wbr></wbr><span class="parameters">(double center, double extent)</span>

    </div>

    <div class="block">

    Constructs an AngleRange from the provided center angle defining the direction and an angular width to extent the range by 50% clockwise and 50% counter-clockwise from its center angle. Corrects values if they exceed the ranges. Example: direction = 90, extent = 10 means the circle sector is pointing east, with an extent of 5 degrees north-wards and 5 degrees south-wards.

    </div>

    Parameters:  
    `center` -

    Start angle, running clockwise, in degrees from north. The value will be normalized to \[0.0, 360.0).

    `extent` -

    The range's extent, running clockwise, in degrees from start. The value will be clamped to the range of \[0, 360\] degrees.

    Returns:  
    Created AngleRange from the provided center angle and the range's extent.

    </div>

  - <div id="sdk-for-android-explore-inRange-double" class="section detail">

    ### inRange

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">inRange</span><wbr></wbr><span class="parameters">(double angleClockwiseInDegreesFromNorth)</span>

    </div>

    <div class="block">

    Check if a given angle in degrees, clockwise from north is in range or not.

    </div>

    Parameters:  
    `angleClockwiseInDegreesFromNorth` -

    An angle in degrees from north. Will be normalized before testing.

    Returns:  
    `True`, if an angle is in range, `false` otherwise.

    </div>

  - <div id="sdk-for-android-explore-closestInRange-double" class="section detail">

    ### closestInRange

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">closestInRange</span><wbr></wbr><span class="parameters">(double angleClockwiseInDegreesFromNorth)</span>

    </div>

    <div class="block">

    Get the angle that is closest to the given one and in range. If the angle to both ends of the range is the same, the value in the clockwise direction is returned. If the given angle is in range already, it will be returned as normalized angle.

    </div>

    Parameters:  
    `angleClockwiseInDegreesFromNorth` -

    An angle in degrees from north. Will be normalized.

    Returns:  
    The closest, normalized in-range angle in degrees, clockwise from north. If the given angle is in range already, the given angle will be returned as normalized angle in degree, clockwise from north.

    </div>

  - <div id="sdk-for-android-explore-max" class="section detail">

    ### max

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">max</span>()

    </div>

    <div class="block">

    Get the maximum angle defined by the range in degrees, clockwise from north, normalized to \[0,360).

    </div>

    Returns:  
    Maximum angle of the range in degrees, clockwise from north, normalized to \[0,360).

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

