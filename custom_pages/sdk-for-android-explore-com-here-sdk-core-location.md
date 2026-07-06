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

<div id="sdk-for-android-explore-class-description"
class="section class-description">

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
<div id="sdk-for-android-explore-field-summary"
  class="section field-summary">

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

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-location#bearingAccuracyInDegrees"
  class="member-name-link"><code>bearingAccuracyInDegrees</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Estimated bearing accuracy for this location, in degrees.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-location#bearingInDegrees"
  class="member-name-link"><code>bearingInDegrees</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Bearing (also known as course) is the device's horizontal direction of
  travel.

  </div>

  </div>

  <div class="col-first even-row-color">

  [`GeoCoordinates`](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-core-location#coordinates"
  class="member-name-link"><code>coordinates</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The geographic coordinates of the location.

  </div>

  </div>

  <div class="col-first odd-row-color">

  [`Duration`](sdk-for-android-explore-com-here-time-duration "class in com.here.time")

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-core-location#gnssTime"
  class="member-name-link"><code>gnssTime</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Optional gnss time at which the location was determined.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-location#horizontalAccuracyInMeters"
  class="member-name-link"><code>horizontalAccuracyInMeters</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The estimated horizontal accuracy.

  </div>

  </div>

  <div class="col-first odd-row-color">

  [`LocationTechnology`](sdk-for-android-explore-com-here-sdk-core-locationtechnology "enum class in com.here.sdk.core")

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-location#locationTechnology"
  class="member-name-link"><code>locationTechnology</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Optional technology or provider of this location.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-location#pitchInDegrees"
  class="member-name-link"><code>pitchInDegrees</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Pitch of this location, in degrees.

  </div>

  </div>

  <div class="col-first odd-row-color">

  [`LocationSource`](sdk-for-android-explore-com-here-sdk-core-locationsource "enum class in com.here.sdk.core")

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-core-location#source"
  class="member-name-link"><code>source</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Optional source of this location.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-location#speedAccuracyInMetersPerSecond"
  class="member-name-link"><code>speedAccuracyInMetersPerSecond</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Estimated speed accuracy of this location, in meters per second.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-location#speedInMetersPerSecond"
  class="member-name-link"><code>speedInMetersPerSecond</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Current speed of the device.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html"
  class="external-link"
  title="class or interface in java.util"><code>Date</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-core-location#time"
  class="member-name-link"><code>time</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The time at which the location was determined.

  </div>

  </div>

  <div class="col-first odd-row-color">

  [`Duration`](sdk-for-android-explore-com-here-time-duration "class in com.here.time")

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-location#timestampSinceBoot"
  class="member-name-link"><code>timestampSinceBoot</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The time at which the location was determined, relative to device boot
  time.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-location#verticalAccuracyInMeters"
  class="member-name-link"><code>verticalAccuracyInMeters</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Estimated vertical accuracy.

  </div>

  </div>

  </div>

  </div>
<div id="sdk-for-android-explore-constructor-summary"
  class="section constructor-summary">

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

      Location(GeoCoordinates coordinates)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new Location instance from the provided GeoCoordinates
  value.

  </div>

  </div>

  </div>

  </div>
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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      equals(Object obj)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

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
<div id="sdk-for-android-explore-field-detail"
  class="section field-details">
<div id="sdk-for-android-explore-coordinates"
    class="section detail">

    ### coordinates

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")</span> <span class="element-name">coordinates</span>

    </div>

    <div class="block">

    The geographic coordinates of the location.

    </div>

    </div>
<div id="sdk-for-android-explore-bearingInDegrees"
    class="section detail">

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
<div id="sdk-for-android-explore-speedInMetersPerSecond"
    class="section detail">

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
<div id="sdk-for-android-explore-time" class="section detail">

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
<div id="sdk-for-android-explore-horizontalAccuracyInMeters"
    class="section detail">

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
<div id="sdk-for-android-explore-verticalAccuracyInMeters"
    class="section detail">

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
<div id="sdk-for-android-explore-bearingAccuracyInDegrees"
    class="section detail">

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
<div id="sdk-for-android-explore-speedAccuracyInMetersPerSecond"
    class="section detail">

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
<div id="sdk-for-android-explore-timestampSinceBoot"
    class="section detail">

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
<div id="sdk-for-android-explore-locationTechnology"
    class="section detail">

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
<div id="sdk-for-android-explore-source" class="section detail">

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
<div id="sdk-for-android-explore-gnssTime" class="section detail">

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
<div id="sdk-for-android-explore-pitchInDegrees"
    class="section detail">

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
<div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">
<div id="sdk-for-android-explore-<init>(com.here.sdk.core.GeoCoordinates)"
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
<div id="sdk-for-android-explore-method-detail"
  class="section method-details">
<div id="sdk-for-android-explore-equals(java.lang.Object)"
    class="section detail">

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
<div id="sdk-for-android-explore-hashCode()" class="section detail">

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

