---
title: "Duration (API Reference)"
slug: "sdk-for-android-explore-com-here-time-duration"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.time](sdk-for-android-explore-com-here-time-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.time.Duration → com.here.time.Duration

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

All Implemented Interfaces:  
<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" class="external-link" title="class or interface in java.lang"><code>Comparable</code></a>`<`[`Duration`](sdk-for-android-explore-com-here-time-duration "class in com.here.time")`>`

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">Duration</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a> implements <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" class="external-link" title="class or interface in java.lang">Comparable</a>\<[Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time")\></span>

</div>

<div class="block">

Represents duration in time (both positive and negative). The duration is represented as number of seconds (see getSeconds() ) and number of nanonseconds in a second (see getNano() ). Duration can be created from various units of time by calling on of of\* methods. The to\* family of methods convert duration to a value expressed in desired unit of time.

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

  `int`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      compareTo ( Duration duration)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      equals ( Object o)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getNano ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `long`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getSeconds ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `[`Duration`](sdk-for-android-explore-com-here-time-duration "class in com.here.time")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      ofDays (long days)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Creates a duration representing specified number of days.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `[`Duration`](sdk-for-android-explore-com-here-time-duration "class in com.here.time")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      ofHours (long hours)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Creates a duration representing specified number of hours.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `[`Duration`](sdk-for-android-explore-com-here-time-duration "class in com.here.time")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      ofMillis (long milliseconds)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Creates a duration representing specified number of milliseconds.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `[`Duration`](sdk-for-android-explore-com-here-time-duration "class in com.here.time")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      ofMinutes (long minutes)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Creates a duration representing specified number of hours.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `[`Duration`](sdk-for-android-explore-com-here-time-duration "class in com.here.time")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      ofNanos (long nanoseconds)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Creates a duration representing specified number of nanoseconds.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `[`Duration`](sdk-for-android-explore-com-here-time-duration "class in com.here.time")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      ofSeconds (long seconds)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Creates a duration representing specified number of seconds.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `[`Duration`](sdk-for-android-explore-com-here-time-duration "class in com.here.time")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      ofSeconds (long seconds,
       long nanoAdjustment)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Creates a duration representing specified number of seconds and an adjustment in nanoseconds.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `long`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      toDays ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Converts this duration to days.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `long`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      toDaysPart ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Same as toDays() .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `long`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      toHours ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Converts this duration to hours.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      toHoursPart ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the hours part of this duration.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `long`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      toMillis ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Converts this duration to milliseconds.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      toMillisPart ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the milliseconds part of this duration.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `long`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      toMinutes ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Converts this duration to minutes.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      toMinutesPart ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the minutes part of this duration.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `long`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      toNanos ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Converts this duration to nanoseconds.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      toNanosPart ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the nanoseconds part of this duration.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `long`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      toSeconds ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Converts this duration to seconds.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      toSecondsPart ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the seconds part of this duration.

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

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-getNano" class="section detail">

    ### getNano

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getNano</span>()

    </div>

    Returns:  
    The nanoseconds component of this duration.

    </div>

  - <div id="sdk-for-android-explore-getSeconds" class="section detail">

    ### getSeconds

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">getSeconds</span>()

    </div>

    Returns:  
    The seconds component of this duration.

    </div>

  - <div id="sdk-for-android-explore-ofDays-long" class="section detail">

    ### ofDays

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type">[Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time")</span> <span class="element-name">ofDays</span><wbr></wbr><span class="parameters">(long days)</span> throws <span class="exceptions"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html" class="external-link" title="class or interface in java.lang">ArithmeticException</a></span>

    </div>

    <div class="block">

    Creates a duration representing specified number of days. A Day is assumed to always be 24 hours.

    </div>

    Parameters:  
    `days` - The number of days.

    Returns:  
    The Duration representing the specified number of days.

    Throws:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html" class="external-link" title="class or interface in java.lang"><code>ArithmeticException</code></a> - if the input is outside the range possible to represent by a Duration

    </div>

  - <div id="sdk-for-android-explore-ofHours-long" class="section detail">

    ### ofHours

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type">[Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time")</span> <span class="element-name">ofHours</span><wbr></wbr><span class="parameters">(long hours)</span> throws <span class="exceptions"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html" class="external-link" title="class or interface in java.lang">ArithmeticException</a></span>

    </div>

    <div class="block">

    Creates a duration representing specified number of hours. An hour is assumed to always be 60 minutes.

    </div>

    Parameters:  
    `hours` - The number of hours.

    Returns:  
    The Duration representing the specified number of hours.

    Throws:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html" class="external-link" title="class or interface in java.lang"><code>ArithmeticException</code></a> - if the input is outside the range possible to represent by a Duration

    </div>

  - <div id="sdk-for-android-explore-ofMinutes-long" class="section detail">

    ### ofMinutes

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type">[Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time")</span> <span class="element-name">ofMinutes</span><wbr></wbr><span class="parameters">(long minutes)</span> throws <span class="exceptions"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html" class="external-link" title="class or interface in java.lang">ArithmeticException</a></span>

    </div>

    <div class="block">

    Creates a duration representing specified number of hours. A minute is assumed to always be 60 seconds.

    </div>

    Parameters:  
    `minutes` - The number of minutes.

    Returns:  
    The Duration representing the specified number of minutes.

    Throws:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html" class="external-link" title="class or interface in java.lang"><code>ArithmeticException</code></a> - if the input is outside the range possible to represent by a Duration

    </div>

  - <div id="sdk-for-android-explore-ofSeconds-long" class="section detail">

    ### ofSeconds

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type">[Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time")</span> <span class="element-name">ofSeconds</span><wbr></wbr><span class="parameters">(long seconds)</span>

    </div>

    <div class="block">

    Creates a duration representing specified number of seconds.

    </div>

    Parameters:  
    `seconds` - The number of seconds.

    Returns:  
    The Duration representing the specified number of seconds.

    </div>

  - <div id="sdk-for-android-explore-ofSeconds-long-long" class="section detail">

    ### ofSeconds

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type">[Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time")</span> <span class="element-name">ofSeconds</span><wbr></wbr><span class="parameters">(long seconds, long nanoAdjustment)</span>

    </div>

    <div class="block">

    Creates a duration representing specified number of seconds and an adjustment in nanoseconds.

    </div>

    Parameters:  
    `seconds` - The number of seconds.

    `nanoAdjustment` - The nanosecond adjustment to the number of seconds.

    Returns:  
    The Duration representing the specified number of seconds, adjusted.

    </div>

  - <div id="sdk-for-android-explore-ofMillis-long" class="section detail">

    ### ofMillis

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type">[Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time")</span> <span class="element-name">ofMillis</span><wbr></wbr><span class="parameters">(long milliseconds)</span>

    </div>

    <div class="block">

    Creates a duration representing specified number of milliseconds.

    </div>

    Parameters:  
    `milliseconds` - The number of milliseconds.

    Returns:  
    The Duration representing the specified number of milliseconds.

    </div>

  - <div id="sdk-for-android-explore-ofNanos-long" class="section detail">

    ### ofNanos

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type">[Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time")</span> <span class="element-name">ofNanos</span><wbr></wbr><span class="parameters">(long nanoseconds)</span>

    </div>

    <div class="block">

    Creates a duration representing specified number of nanoseconds.

    </div>

    Parameters:  
    `nanoseconds` - The number of nanoseconds.

    Returns:  
    The Duration representing the specified number of nanoseconds.

    </div>

  - <div id="sdk-for-android-explore-toNanos" class="section detail">

    ### toNanos

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">toNanos</span>() throws <span class="exceptions"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html" class="external-link" title="class or interface in java.lang">ArithmeticException</a></span>

    </div>

    <div class="block">

    Converts this duration to nanoseconds.

    </div>

    Returns:  
    Total number of nanoseconds in this duration.

    Throws:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html" class="external-link" title="class or interface in java.lang"><code>ArithmeticException</code></a> - if the resulting value cannot be represented by `long` type.

    </div>

  - <div id="sdk-for-android-explore-toNanosPart" class="section detail">

    ### toNanosPart

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">toNanosPart</span>()

    </div>

    <div class="block">

    Gets the nanoseconds part of this duration. Equals to getNano() .

    </div>

    Returns:  
    The nanoseconds part of this duration, value from 0 to 999999999.

    </div>

  - <div id="sdk-for-android-explore-toMillis" class="section detail">

    ### toMillis

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">toMillis</span>() throws <span class="exceptions"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html" class="external-link" title="class or interface in java.lang">ArithmeticException</a></span>

    </div>

    <div class="block">

    Converts this duration to milliseconds. Any data past milliseconds precision is simply discarded. There is no mathematical rounding, so a duration of 999999 nanoseconds will still be converted to 0 milliseconds.

    </div>

    Returns:  
    Total number of milliseconds in this duration.

    Throws:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html" class="external-link" title="class or interface in java.lang"><code>ArithmeticException</code></a> - if the resulting value cannot be represented by `long` type.

    </div>

  - <div id="sdk-for-android-explore-toMillisPart" class="section detail">

    ### toMillisPart

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">toMillisPart</span>()

    </div>

    <div class="block">

    Gets the milliseconds part of this duration.

    </div>

    Returns:  
    The milliseconds part of this duration.

    </div>

  - <div id="sdk-for-android-explore-toSeconds" class="section detail">

    ### toSeconds

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">toSeconds</span>()

    </div>

    <div class="block">

    Converts this duration to seconds. Any data past seconds precision is simply discarded. There is no mathematical rounding, so a duration of 999 milliseconds will still be converted to 0 seconds.

    </div>

    Returns:  
    Total number of seconds in this duration.

    </div>

  - <div id="sdk-for-android-explore-toSecondsPart" class="section detail">

    ### toSecondsPart

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">toSecondsPart</span>()

    </div>

    <div class="block">

    Gets the seconds part of this duration.

    </div>

    Returns:  
    The seconds part of this duration, value from 0 to 59.

    </div>

  - <div id="sdk-for-android-explore-toMinutes" class="section detail">

    ### toMinutes

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">toMinutes</span>()

    </div>

    <div class="block">

    Converts this duration to minutes. Any data past minute precision is simply discarded. There is no mathematical rounding, so a duration of 59 seconds and 999 milliseconds will still be converted to 0 minutes.

    </div>

    Returns:  
    Total number of minutes in this duration.

    </div>

  - <div id="sdk-for-android-explore-toMinutesPart" class="section detail">

    ### toMinutesPart

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">toMinutesPart</span>()

    </div>

    <div class="block">

    Gets the minutes part of this duration.

    </div>

    Returns:  
    The minutes part of this duration, value from 0 to 59.

    </div>

  - <div id="sdk-for-android-explore-toHours" class="section detail">

    ### toHours

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">toHours</span>()

    </div>

    <div class="block">

    Converts this duration to hours. Any data past hour precision is simply discarded. There is no mathematical rounding, so a duration of 59 minutes and 59 seconds will still be converted to 0 hours.

    </div>

    Returns:  
    The number of full hours in this duration.

    </div>

  - <div id="sdk-for-android-explore-toHoursPart" class="section detail">

    ### toHoursPart

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">toHoursPart</span>()

    </div>

    <div class="block">

    Gets the hours part of this duration.

    </div>

    Returns:  
    The hours part of this duration, value from 0 to 23.

    </div>

  - <div id="sdk-for-android-explore-toDays" class="section detail">

    ### toDays

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">toDays</span>()

    </div>

    <div class="block">

    Converts this duration to days. Any data past day precision is simply discarded. There is no mathematical rounding, so a duration of 23 hours 59 minutes and 59 seconds will still be converted to 0 days. Day is always assumed to be 24 hours.

    </div>

    Returns:  
    The number of full days in this duration.

    </div>

  - <div id="sdk-for-android-explore-toDaysPart" class="section detail">

    ### toDaysPart

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">toDaysPart</span>()

    </div>

    <div class="block">

    Same as toDays() .

    </div>

    Returns:  
    The number of full days in this duration.

    </div>

  - <div id="sdk-for-android-explore-compareTo-com-here-time-Duration" class="section detail">

    ### compareTo

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">compareTo</span><wbr></wbr><span class="parameters">([Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time") duration)</span>

    </div>

    Specified by:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" class="external-link" title="class or interface in java.lang"><code>compareTo</code></a> in interface <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" class="external-link" title="class or interface in java.lang"><code>Comparable</code></a>`<`[`Duration`](sdk-for-android-explore-com-here-time-duration "class in com.here.time")`>`

    </div>

  - <div id="sdk-for-android-explore-equals-java-lang-Object" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a> o)</span>

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

  </div>

<!-- ========= END OF CLASS DATA ========= -->

