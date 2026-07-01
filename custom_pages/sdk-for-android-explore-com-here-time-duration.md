---
title: "Duration (API Reference)"
slug: "sdk-for-android-explore-com-here-time-duration"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.time](sdk-for-android-explore-com-here-time-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.time.Duration

</div>

<div id="class-description" class="section class-description">

All Implemented Interfaces:  
<a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html"
class="external-link"
title="class or interface in java.lang"><code>Comparable</code></a>`<`[`Duration`](sdk-for-android-explore-com-here-time-duration "class in com.here.time")`>`

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">Duration</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a>
implements <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html"
class="external-link"
title="class or interface in java.lang">Comparable</a><[Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time")></span>

</div>

<div class="block">

Represents duration in time (both positive and negative). The duration
is represented as number of seconds (see getSeconds() ) and number of
nanonseconds in a second (see getNano() ). Duration can be created from
various units of time by calling on of of\* methods. The to\* family of
methods convert duration to a value expressed in desired unit of time.

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
  <td><code>int</code></td>
  <td><pre><code>compareTo(Duration duration)</code></pre></td>
  <td> </td>
  </tr>
  <tr>
  <td><code>boolean</code></td>
  <td><pre><code>equals(Object o)</code></pre></td>
  <td> </td>
  </tr>
  <tr>
  <td><code>int</code></td>
  <td><pre><code>getNano()</code></pre></td>
  <td> </td>
  </tr>
  <tr>
  <td><code>long</code></td>
  <td><pre><code>getSeconds()</code></pre></td>
  <td> </td>
  </tr>
  <tr>
  <td><code>int</code></td>
  <td><pre><code>hashCode()</code></pre></td>
  <td> </td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-time-duration"
  title="class in com.here.time"><code>Duration</code></a></td>
  <td><pre><code>ofDays(long days)</code></pre></td>
  <td><div class="block">
  Creates a duration representing specified number of days.
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-time-duration"
  title="class in com.here.time"><code>Duration</code></a></td>
  <td><pre><code>ofHours(long hours)</code></pre></td>
  <td><div class="block">
  Creates a duration representing specified number of hours.
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-time-duration"
  title="class in com.here.time"><code>Duration</code></a></td>
  <td><pre><code>ofMillis(long milliseconds)</code></pre></td>
  <td><div class="block">
  Creates a duration representing specified number of milliseconds.
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-time-duration"
  title="class in com.here.time"><code>Duration</code></a></td>
  <td><pre><code>ofMinutes(long minutes)</code></pre></td>
  <td><div class="block">
  Creates a duration representing specified number of hours.
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-time-duration"
  title="class in com.here.time"><code>Duration</code></a></td>
  <td><pre><code>ofNanos(long nanoseconds)</code></pre></td>
  <td><div class="block">
  Creates a duration representing specified number of nanoseconds.
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-time-duration"
  title="class in com.here.time"><code>Duration</code></a></td>
  <td><pre><code>ofSeconds(long seconds)</code></pre></td>
  <td><div class="block">
  Creates a duration representing specified number of seconds.
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-time-duration"
  title="class in com.here.time"><code>Duration</code></a></td>
  <td><pre><code>ofSeconds(long seconds,
   long nanoAdjustment)</code></pre></td>
  <td><div class="block">
  Creates a duration representing specified number of seconds and an
  adjustment in nanoseconds.
  </div></td>
  </tr>
  <tr>
  <td><code>long</code></td>
  <td><pre><code>toDays()</code></pre></td>
  <td><div class="block">
  Converts this duration to days.
  </div></td>
  </tr>
  <tr>
  <td><code>long</code></td>
  <td><pre><code>toDaysPart()</code></pre></td>
  <td><div class="block">
  Same as toDays() .
  </div></td>
  </tr>
  <tr>
  <td><code>long</code></td>
  <td><pre><code>toHours()</code></pre></td>
  <td><div class="block">
  Converts this duration to hours.
  </div></td>
  </tr>
  <tr>
  <td><code>int</code></td>
  <td><pre><code>toHoursPart()</code></pre></td>
  <td><div class="block">
  Gets the hours part of this duration.
  </div></td>
  </tr>
  <tr>
  <td><code>long</code></td>
  <td><pre><code>toMillis()</code></pre></td>
  <td><div class="block">
  Converts this duration to milliseconds.
  </div></td>
  </tr>
  <tr>
  <td><code>int</code></td>
  <td><pre><code>toMillisPart()</code></pre></td>
  <td><div class="block">
  Gets the milliseconds part of this duration.
  </div></td>
  </tr>
  <tr>
  <td><code>long</code></td>
  <td><pre><code>toMinutes()</code></pre></td>
  <td><div class="block">
  Converts this duration to minutes.
  </div></td>
  </tr>
  <tr>
  <td><code>int</code></td>
  <td><pre><code>toMinutesPart()</code></pre></td>
  <td><div class="block">
  Gets the minutes part of this duration.
  </div></td>
  </tr>
  <tr>
  <td><code>long</code></td>
  <td><pre><code>toNanos()</code></pre></td>
  <td><div class="block">
  Converts this duration to nanoseconds.
  </div></td>
  </tr>
  <tr>
  <td><code>int</code></td>
  <td><pre><code>toNanosPart()</code></pre></td>
  <td><div class="block">
  Gets the nanoseconds part of this duration.
  </div></td>
  </tr>
  <tr>
  <td><code>long</code></td>
  <td><pre><code>toSeconds()</code></pre></td>
  <td><div class="block">
  Converts this duration to seconds.
  </div></td>
  </tr>
  <tr>
  <td><code>int</code></td>
  <td><pre><code>toSecondsPart()</code></pre></td>
  <td><div class="block">
  Gets the seconds part of this duration.
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

  - <div id="getNano()" class="section detail">

    ### getNano

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getNano</span>()

    </div>

    Returns:  
    The nanoseconds component of this duration.

    </div>

  - <div id="getSeconds()" class="section detail">

    ### getSeconds

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">getSeconds</span>()

    </div>

    Returns:  
    The seconds component of this duration.

    </div>

  - <div id="ofDays(long)" class="section detail">

    ### ofDays

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">[Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time")</span> <span class="element-name">ofDays</span><span class="parameters">(long days)</span>
    throws <span class="exceptions"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html"
    class="external-link"
    title="class or interface in java.lang">ArithmeticException</a></span>

    </div>

    <div class="block">

    Creates a duration representing specified number of days. A Day is
    assumed to always be 24 hours.

    </div>

    Parameters:  
    `days` - The number of days.

    Returns:  
    The Duration representing the specified number of days.

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html"
    class="external-link"
    title="class or interface in java.lang"><code>ArithmeticException</code></a> -
    if the input is outside the range possible to represent by a
    Duration

    </div>

  - <div id="ofHours(long)" class="section detail">

    ### ofHours

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">[Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time")</span> <span class="element-name">ofHours</span><span class="parameters">(long hours)</span>
    throws <span class="exceptions"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html"
    class="external-link"
    title="class or interface in java.lang">ArithmeticException</a></span>

    </div>

    <div class="block">

    Creates a duration representing specified number of hours. An hour
    is assumed to always be 60 minutes.

    </div>

    Parameters:  
    `hours` - The number of hours.

    Returns:  
    The Duration representing the specified number of hours.

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html"
    class="external-link"
    title="class or interface in java.lang"><code>ArithmeticException</code></a> -
    if the input is outside the range possible to represent by a
    Duration

    </div>

  - <div id="ofMinutes(long)" class="section detail">

    ### ofMinutes

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">[Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time")</span> <span class="element-name">ofMinutes</span><span class="parameters">(long minutes)</span>
    throws <span class="exceptions"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html"
    class="external-link"
    title="class or interface in java.lang">ArithmeticException</a></span>

    </div>

    <div class="block">

    Creates a duration representing specified number of hours. A minute
    is assumed to always be 60 seconds.

    </div>

    Parameters:  
    `minutes` - The number of minutes.

    Returns:  
    The Duration representing the specified number of minutes.

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html"
    class="external-link"
    title="class or interface in java.lang"><code>ArithmeticException</code></a> -
    if the input is outside the range possible to represent by a
    Duration

    </div>

  - <div id="ofSeconds(long)" class="section detail">

    ### ofSeconds

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">[Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time")</span> <span class="element-name">ofSeconds</span><span class="parameters">(long seconds)</span>

    </div>

    <div class="block">

    Creates a duration representing specified number of seconds.

    </div>

    Parameters:  
    `seconds` - The number of seconds.

    Returns:  
    The Duration representing the specified number of seconds.

    </div>

  - <div id="ofSeconds(long,long)" class="section detail">

    ### ofSeconds

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">[Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time")</span> <span class="element-name">ofSeconds</span><span class="parameters">(long seconds,
    long nanoAdjustment)</span>

    </div>

    <div class="block">

    Creates a duration representing specified number of seconds and an
    adjustment in nanoseconds.

    </div>

    Parameters:  
    `seconds` - The number of seconds.

    `nanoAdjustment` - The nanosecond adjustment to the number of
    seconds.

    Returns:  
    The Duration representing the specified number of seconds, adjusted.

    </div>

  - <div id="ofMillis(long)" class="section detail">

    ### ofMillis

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">[Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time")</span> <span class="element-name">ofMillis</span><span class="parameters">(long milliseconds)</span>

    </div>

    <div class="block">

    Creates a duration representing specified number of milliseconds.

    </div>

    Parameters:  
    `milliseconds` - The number of milliseconds.

    Returns:  
    The Duration representing the specified number of milliseconds.

    </div>

  - <div id="ofNanos(long)" class="section detail">

    ### ofNanos

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">[Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time")</span> <span class="element-name">ofNanos</span><span class="parameters">(long nanoseconds)</span>

    </div>

    <div class="block">

    Creates a duration representing specified number of nanoseconds.

    </div>

    Parameters:  
    `nanoseconds` - The number of nanoseconds.

    Returns:  
    The Duration representing the specified number of nanoseconds.

    </div>

  - <div id="toNanos()" class="section detail">

    ### toNanos

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">toNanos</span>()
    throws <span class="exceptions"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html"
    class="external-link"
    title="class or interface in java.lang">ArithmeticException</a></span>

    </div>

    <div class="block">

    Converts this duration to nanoseconds.

    </div>

    Returns:  
    Total number of nanoseconds in this duration.

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html"
    class="external-link"
    title="class or interface in java.lang"><code>ArithmeticException</code></a> -
    if the resulting value cannot be represented by `long` type.

    </div>

  - <div id="toNanosPart()" class="section detail">

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

  - <div id="toMillis()" class="section detail">

    ### toMillis

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">toMillis</span>()
    throws <span class="exceptions"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html"
    class="external-link"
    title="class or interface in java.lang">ArithmeticException</a></span>

    </div>

    <div class="block">

    Converts this duration to milliseconds. Any data past milliseconds
    precision is simply discarded. There is no mathematical rounding, so
    a duration of 999999 nanoseconds will still be converted to 0
    milliseconds.

    </div>

    Returns:  
    Total number of milliseconds in this duration.

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html"
    class="external-link"
    title="class or interface in java.lang"><code>ArithmeticException</code></a> -
    if the resulting value cannot be represented by `long` type.

    </div>

  - <div id="toMillisPart()" class="section detail">

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

  - <div id="toSeconds()" class="section detail">

    ### toSeconds

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">toSeconds</span>()

    </div>

    <div class="block">

    Converts this duration to seconds. Any data past seconds precision
    is simply discarded. There is no mathematical rounding, so a
    duration of 999 milliseconds will still be converted to 0 seconds.

    </div>

    Returns:  
    Total number of seconds in this duration.

    </div>

  - <div id="toSecondsPart()" class="section detail">

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

  - <div id="toMinutes()" class="section detail">

    ### toMinutes

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">toMinutes</span>()

    </div>

    <div class="block">

    Converts this duration to minutes. Any data past minute precision is
    simply discarded. There is no mathematical rounding, so a duration
    of 59 seconds and 999 milliseconds will still be converted to 0
    minutes.

    </div>

    Returns:  
    Total number of minutes in this duration.

    </div>

  - <div id="toMinutesPart()" class="section detail">

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

  - <div id="toHours()" class="section detail">

    ### toHours

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">toHours</span>()

    </div>

    <div class="block">

    Converts this duration to hours. Any data past hour precision is
    simply discarded. There is no mathematical rounding, so a duration
    of 59 minutes and 59 seconds will still be converted to 0 hours.

    </div>

    Returns:  
    The number of full hours in this duration.

    </div>

  - <div id="toHoursPart()" class="section detail">

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

  - <div id="toDays()" class="section detail">

    ### toDays

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">toDays</span>()

    </div>

    <div class="block">

    Converts this duration to days. Any data past day precision is
    simply discarded. There is no mathematical rounding, so a duration
    of 23 hours 59 minutes and 59 seconds will still be converted to 0
    days. Day is always assumed to be 24 hours.

    </div>

    Returns:  
    The number of full days in this duration.

    </div>

  - <div id="toDaysPart()" class="section detail">

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

  - <div id="compareTo(com.here.time.Duration)" class="section detail">

    ### compareTo

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">compareTo</span><span class="parameters">([Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time") duration)</span>

    </div>

    Specified by:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T)"
    class="external-link"
    title="class or interface in java.lang"><code>compareTo</code></a> in
    interface <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html"
    class="external-link"
    title="class or interface in java.lang"><code>Comparable</code></a>`<`[`Duration`](sdk-for-android-explore-com-here-time-duration "class in com.here.time")`>`

    </div>

  - <div id="equals(java.lang.Object)" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><span class="parameters">(<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link" title="class or interface in java.lang">Object</a> o)</span>

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

