---
title: "Location (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-location"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core](sdk-for-android-explore-com-here-sdk-core-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.core.Location

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">Location</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Describes a location in the world at a given time.

</div>

</div>

<div class="section summary">

- <div id="field-summary" class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Field</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-location#bearingAccuracyInDegrees"
  class="member-name-link"><code>bearingAccuracyInDegrees</code></a></td>
  <td><div class="block">
  Estimated bearing accuracy for this location, in degrees.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-location#bearingInDegrees"
  class="member-name-link"><code>bearingInDegrees</code></a></td>
  <td><div class="block">
  Bearing (also known as course) is the device's horizontal direction of
  travel.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates"
  title="class in com.here.sdk.core"><code>GeoCoordinates</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-location#coordinates"
  class="member-name-link"><code>coordinates</code></a></td>
  <td><div class="block">
  The geographic coordinates of the location.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-time-duration"
  title="class in com.here.time"><code>Duration</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-location#gnssTime"
  class="member-name-link"><code>gnssTime</code></a></td>
  <td><div class="block">
  Optional gnss time at which the location was determined.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-location#horizontalAccuracyInMeters"
  class="member-name-link"><code>horizontalAccuracyInMeters</code></a></td>
  <td><div class="block">
  The estimated horizontal accuracy.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-locationtechnology"
  title="enum class in com.here.sdk.core"><code>LocationTechnology</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-location#locationTechnology"
  class="member-name-link"><code>locationTechnology</code></a></td>
  <td><div class="block">
  Optional technology or provider of this location.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-location#pitchInDegrees"
  class="member-name-link"><code>pitchInDegrees</code></a></td>
  <td><div class="block">
  Pitch of this location, in degrees.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-locationsource"
  title="enum class in com.here.sdk.core"><code>LocationSource</code></a></td>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-location#source"
  class="member-name-link"><code>source</code></a></td>
  <td><div class="block">
  Optional source of this location.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-location#speedAccuracyInMetersPerSecond"
  class="member-name-link"><code>speedAccuracyInMetersPerSecond</code></a></td>
  <td><div class="block">
  Estimated speed accuracy of this location, in meters per second.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-location#speedInMetersPerSecond"
  class="member-name-link"><code>speedInMetersPerSecond</code></a></td>
  <td><div class="block">
  Current speed of the device.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html"
  class="external-link"
  title="class or interface in java.util"><code>Date</code></a></td>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-location#time"
  class="member-name-link"><code>time</code></a></td>
  <td><div class="block">
  The time at which the location was determined.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-time-duration"
  title="class in com.here.time"><code>Duration</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-location#timestampSinceBoot"
  class="member-name-link"><code>timestampSinceBoot</code></a></td>
  <td><div class="block">
  The time at which the location was determined, relative to device boot
  time.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-location#verticalAccuracyInMeters"
  class="member-name-link"><code>verticalAccuracyInMeters</code></a></td>
  <td><div class="block">
  Estimated vertical accuracy.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

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
  <td><pre><code>Location(GeoCoordinates coordinates)</code></pre></td>
  <td><div class="block">
  Creates a new Location instance from the provided GeoCoordinates value.
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
  <td><pre><code>equals(Object obj)</code></pre></td>
  <td> </td>
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

- <div id="field-detail" class="section field-details">

  - <div id="coordinates" class="section detail">

    ### coordinates

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")</span> <span class="element-name">coordinates</span>

    </div>

    <div class="block">

    The geographic coordinates of the location.

    </div>

    </div>

  - <div id="bearingInDegrees" class="section detail">

    ### bearingInDegrees

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">bearingInDegrees</span>

    </div>

    <div class="block">

    Bearing (also known as course) is the device's horizontal direction
    of travel. Starts at 0 in the geographical north and rotates around
    the compass in a clockwise direction. This means for going north it
    is equal to 0, for northeast it is 45, for east it is 90 and so on.
    Note that this may be different from the orientation of the device.
    If it cannot be determined, the value is null . Otherwise, it is
    guaranteed to be in the range \[0, 360).

    </div>

    </div>

  - <div id="speedInMetersPerSecond" class="section detail">

    ### speedInMetersPerSecond

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">speedInMetersPerSecond</span>

    </div>

    <div class="block">

    Current speed of the device. If it cannot be determined, the value
    is null .

    </div>

    </div>

  - <div id="time" class="section detail">

    ### time

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html"
    class="external-link" title="class or interface in java.util">Date</a></span> <span class="element-name">time</span>

    </div>

    <div class="block">

    The time at which the location was determined.

    </div>

    </div>

  - <div id="horizontalAccuracyInMeters" class="section detail">

    ### horizontalAccuracyInMeters

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">horizontalAccuracyInMeters</span>

    </div>

    <div class="block">

    The estimated horizontal accuracy. The actual location will lie
    within this radius of uncertainty.

    </div>

    </div>

  - <div id="verticalAccuracyInMeters" class="section detail">

    ### verticalAccuracyInMeters

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">verticalAccuracyInMeters</span>

    </div>

    <div class="block">

    Estimated vertical accuracy. Given that the received Location
    contains the altitude, the real value of the altitude is estimated
    to lie within the following range: \[altitude - vertical accuracy,
    altitude + vertical accuracy\]. For example, when the altitude is
    equal to 50 and the vertical accuracy is 8, then the actual value is
    most likely in the range \[42, 58\].

    </div>

    </div>

  - <div id="bearingAccuracyInDegrees" class="section detail">

    ### bearingAccuracyInDegrees

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">bearingAccuracyInDegrees</span>

    </div>

    <div class="block">

    Estimated bearing accuracy for this location, in degrees. If it
    cannot be determined, the value is null .

    </div>

    </div>

  - <div id="speedAccuracyInMetersPerSecond" class="section detail">

    ### speedAccuracyInMetersPerSecond

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">speedAccuracyInMetersPerSecond</span>

    </div>

    <div class="block">

    Estimated speed accuracy of this location, in meters per second. If
    it cannot be determined, the value is null .

    </div>

    </div>

  - <div id="timestampSinceBoot" class="section detail">

    ### timestampSinceBoot

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time")</span> <span class="element-name">timestampSinceBoot</span>

    </div>

    <div class="block">

    The time at which the location was determined, relative to device
    boot time. This time is monotonic and not affected by leap time or
    other system time adjustments, so this is the recommended basis for
    general purpose interval timing between location updates. If it
    cannot be determined, the value is null .

    </div>

    </div>

  - <div id="locationTechnology" class="section detail">

    ### locationTechnology

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[LocationTechnology](sdk-for-android-explore-com-here-sdk-core-locationtechnology "enum class in com.here.sdk.core")</span> <span class="element-name">locationTechnology</span>

    </div>

    <div class="block">

    Optional technology or provider of this location. If it cannot be
    determined, the value is null .

    </div>

    </div>

  - <div id="source" class="section detail">

    ### source

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[LocationSource](sdk-for-android-explore-com-here-sdk-core-locationsource "enum class in com.here.sdk.core")</span> <span class="element-name">source</span>

    </div>

    <div class="block">

    Optional source of this location. If it cannot be determined, the
    value is null .

    </div>

    </div>

  - <div id="gnssTime" class="section detail">

    ### gnssTime

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time")</span> <span class="element-name">gnssTime</span>

    </div>

    <div class="block">

    Optional gnss time at which the location was determined. It is a
    time interval from the Unix time epoch in milliseconds. If it cannot
    be determined, the value is null .

    </div>

    </div>

  - <div id="pitchInDegrees" class="section detail">

    ### pitchInDegrees

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">pitchInDegrees</span>

    </div>

    <div class="block">

    Pitch of this location, in degrees. If it cannot be determined, the
    value is null .

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(com.here.sdk.core.GeoCoordinates)"
    class="section detail">

    ### Location

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Location</span><span class="parameters">(@NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") coordinates)</span>

    </div>

    <div class="block">

    Creates a new Location instance from the provided GeoCoordinates
    value. timestamp is initialized with January 1, 1970, 00:00:00 GMT
    value. The rest of the fields will be initialized to null.

    </div>

    Parameters:  
    `coordinates` -

    The geographic coordinates of the location.

    </div>

  </div>

- <div id="method-detail" class="section method-details">

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

