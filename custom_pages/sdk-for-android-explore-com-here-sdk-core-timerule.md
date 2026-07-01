---
title: "TimeRule (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-timerule"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core](sdk-for-android-explore-com-here-sdk-core-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.NativeBasecom.here.sdk.core.TimeRule →
com.here.NativeBase → com.here.sdk.core.TimeRule

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">TimeRule</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Used to indicate a time period of one or more intervals in GDF
specification. For example:
-\*(M3f21h2){M9}(M11f12h2){-M9}+(h15){h2}(h20){h2}, which represents:
March 2nd Sunday 02h:00m for 9 months ONLY DURING November 1st Sunday
02h:00m from 9 months ago BUT NOT from 15:00 to 17:00 OR 20:00 to 22:00
The operator \* represents reccuring occurrence, + represents a logical
OR operation and - represents exclusion meaning, BUT NOT operations.
This example string represents a time period that meets the following
criteria: M3f21h2 : M3 denotes third month of the year, i.e. March, f2
stands for the second Sunday of the month (as "f" might indicate
"first", "second", "third", etc.), 1 stands for the day of the week
(1...7, Day of week, Sunday = day 1), and h2 represents the hour of the
day (02:00) in 24 hour format. {M9} : This denotes "for 9 months", with
"M9" standing for nine months. The brackets {} indicate a duration.
M11f12h2 : M11 denotes 11th month of the year, i.e. November, f1 stands
for the first Monday of the month, 2 stands for the day of the week
(1...7, Day of week, Monday = day 2), and h2 represents the hour of the
day (02:00) in 24 hour format. {-M9}: This denotes "9 months ago from
the current stated time", with "-M9" standing for nine months in the
past. (h15){h2}(h20){h2} : 15:00 to 17:00 OR 20:00 to 22:00 The brackets
{} denotes duration, and the negative sign - represents a past duration.
Note: The time period is a logical AND (&&) combination of two
components or points in time and it only applies if a point in time is
in both components. For more advanced examples of TimeRule see here .

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
  <td><pre><code>TimeRule(String timeRule,
   int timeZoneOffsetSeconds,
   String dstSpec)</code></pre></td>
  <td><div class="block">
  Creates a new instance of this class.
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
  <td><code>boolean</code></td>
  <td><pre><code>appliesTo(Date dateTime)</code></pre></td>
  <td> </td>
  </tr>
  <tr>
  <td><code>boolean</code></td>
  <td><pre><code>equals(Object rhs)</code></pre></td>
  <td> </td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><pre><code>getDstSpec()</code></pre></td>
  <td><div class="block">
  Gets the value of day saving time specification, as a string in ISO
  14825 format, for the location where the time rule applies.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><pre><code>getTimeRuleString()</code></pre></td>
  <td><div class="block">
  Gets the value of time rule as a string in ISO 14825 format.
  </div></td>
  </tr>
  <tr>
  <td><code>int</code></td>
  <td><pre><code>getTimeZoneOffsetSeconds()</code></pre></td>
  <td><div class="block">
  Gets the value of time zone offset in seconds for the location where the
  time rule applies.
  </div></td>
  </tr>
  <tr>
  <td><code>int</code></td>
  <td><pre><code>hashCode()</code></pre></td>
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

  - <div id="<init>(java.lang.String,int,java.lang.String)"
    class="section detail">

    ### TimeRule

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">TimeRule</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> timeRule,
    int timeZoneOffsetSeconds, @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> dstSpec)</span>

    </div>

    <div class="block">

    Creates a new instance of this class.

    </div>

    Parameters:  
    `timeRule` -

    The time rule as a string in ISO 14825 format.

    `timeZoneOffsetSeconds` -

    The time zone offset in seconds for the location where the time rule
    applies.

    `dstSpec` -

    Day saving time specification, as a string in ISO 14825 format, for
    the location where the time rule applies.

    </div>

  </div>

- <div id="method-detail" class="section method-details">

  - <div id="equals(java.lang.Object)" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><span class="parameters">(<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link" title="class or interface in java.lang">Object</a> rhs)</span>

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

  - <div id="appliesTo(java.util.Date)" class="section detail">

    ### appliesTo

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">appliesTo</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html"
    class="external-link" title="class or interface in java.util">Date</a> dateTime)</span>

    </div>

    Parameters:  
    `dateTime` -

    date and time that should be used for rule verification.

    Returns:  
    `true` if the time domain rules applies to the given date and time.,
    `false` - otherwise.

    </div>

  - <div id="getTimeRuleString()" class="section detail">

    ### getTimeRuleString

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getTimeRuleString</span>()

    </div>

    <div class="block">

    Gets the value of time rule as a string in ISO 14825 format.

    </div>

    Returns:  
    The time rule as a string in ISO 14825 format.

    </div>

  - <div id="getTimeZoneOffsetSeconds()" class="section detail">

    ### getTimeZoneOffsetSeconds

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getTimeZoneOffsetSeconds</span>()

    </div>

    <div class="block">

    Gets the value of time zone offset in seconds for the location where
    the time rule applies.

    </div>

    Returns:  
    The time zone offset in seconds for the location where the time rule
    applies.

    </div>

  - <div id="getDstSpec()" class="section detail">

    ### getDstSpec

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getDstSpec</span>()

    </div>

    <div class="block">

    Gets the value of day saving time specification, as a string in ISO
    14825 format, for the location where the time rule applies.

    </div>

    Returns:  
    Day saving time specification, as a string in ISO 14825 format, for
    the location where the time rule applies.

    </div>

  </div>

</div>

