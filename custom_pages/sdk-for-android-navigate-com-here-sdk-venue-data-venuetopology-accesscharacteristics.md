---
title: "VenueTopology.AccessCharacteristics (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-data-venuetopology-accesscharacteristics"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-venue-data-package-summary">com.here.sdk.venue.data</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.venue.data.VenueTopology.AccessCharacteristics → com.here.NativeBase com.here.sdk.venue.data.VenueTopology.AccessCharacteristics → com.here.sdk.venue.data.VenueTopology.AccessCharacteristics

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

Enclosing class:  
<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuetopology" title="class in com.here.sdk.venue.data">VenueTopology</a>

<div class="type-signature">

<span class="modifiers">public static final class </span><span class="element-name type-name-label">VenueTopology.AccessCharacteristics</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

Represents the access characreisticas of a topology. Access characteristics is a combination of VenueTransportMode which is suppoted on this topology and the VenueTopology.TopologyDirectionality towards which it is allowed.

</div>

</div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div id="sdk-for-android-navigate-method-summary-table">

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

  <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuetopology-topologydirectionality" title="enum class in com.here.sdk.venue.data">`VenueTopology.TopologyDirectionality`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getDirection ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the topology direction.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-venue-routing-venuetransportmode" title="enum class in com.here.sdk.venue.routing">`VenueTransportMode`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getMode ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the mode of transport.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-getMode" class="section detail">

    ### getMode

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-routing-venuetransportmode" title="enum class in com.here.sdk.venue.routing">VenueTransportMode</a></span> <span class="element-name">getMode</span>()

    </div>

    <div class="block">

    Gets the mode of transport.

    </div>

    Returns:  
    Gets the mode of transport.

    </div>

  - <div id="sdk-for-android-navigate-getDirection" class="section detail">

    ### getDirection

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuetopology-topologydirectionality" title="enum class in com.here.sdk.venue.data">VenueTopology.TopologyDirectionality</a></span> <span class="element-name">getDirection</span>()

    </div>

    <div class="block">

    Gets the topology direction.

    </div>

    Returns:  
    Gets topology direction.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

