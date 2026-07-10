---
title: "VenueService (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-service-venueservice"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-venue-service-package-summary">com.here.sdk.venue.service</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.venue.service.VenueService → com.here.NativeBase com.here.sdk.venue.service.VenueService → com.here.sdk.venue.service.VenueService

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">VenueService</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

Offers methods to download venues. Use of this object does not necessitate Map involvement. Before loading the venues, initialize the venue service with one of the start methods. The venue service is online only. Even if there is a cached venue on the device, the venue service requires an online connection to check if the venue is available for the user.

</div>

</div>

- <div id="sdk-for-android-navigate-nested-class-summary" class="section nested-class-summary">

  <div class="caption">

  Nested Classes

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Class

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  `static enum `

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-venue-service-venueservice-venueoptionalfeature" class="type-name-link" title="enum class in com.here.sdk.venue.service"><code>VenueService.VenueOptionalFeature</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Optional features enum

  </div>

  </div>

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

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      add ( VenueListener listener)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Adds a venue listener.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      add ( VenueMapListener listener)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Adds a venue map listener.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      add ( VenueServiceListener listener)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Adds a service listener.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      addVenueToLoad (int venueId)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Adds a venue to the loading queue.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      addVenueToLoad ( String venueIdentifier)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Adds a venue to the loading queue.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-venue-service-venueserviceinitstatus" title="enum class in com.here.sdk.venue.service">`VenueServiceInitStatus`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getInitStatus ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets an initialization status.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getLanguage ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets an active language in the venue service.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>`>`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getLanguages ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the languages available in the venue service.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      isInitialized ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Checks if the venue service is initialized.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      loadOptionalFeatures ( List < VenueService.VenueOptionalFeature > optionalFeatureList)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Lets user load optional features for current session.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      loadTopologies ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Lets user load topologies for current session

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      remove ( VenueListener listener)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Removes a venue listener.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      remove ( VenueMapListener listener)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Removes a venue map listener.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      remove ( VenueServiceListener listener)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Removes a service listener.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setHrn ( String hrn)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets HRN of platform catalog.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setLabeltextPreference ( List < String > labelTextPref)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets override labelTextPreference for labels.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setLanguage ( String value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets an active language.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      stop ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Stops the venue service.

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

  - <div id="sdk-for-android-navigate-stop" class="section detail">

    ### stop

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">stop</span>()

    </div>

    <div class="block">

    Stops the venue service.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-add-com-here-sdk-venue-service-VenueServiceListener" class="section detail">

    ### add

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">add</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-service-venueservicelistener" title="interface in com.here.sdk.venue.service">VenueServiceListener</a> listener)</span>

    </div>

    <div class="block">

    Adds a service listener. The listener is not added if it is null or is already present in the list of listeners.

    </div>

    Parameters:  
    `listener` -

    The service listener to add.

    </div>

  - <div id="sdk-for-android-navigate-remove-com-here-sdk-venue-service-VenueServiceListener" class="section detail">

    ### remove

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">remove</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-service-venueservicelistener" title="interface in com.here.sdk.venue.service">VenueServiceListener</a> listener)</span>

    </div>

    <div class="block">

    Removes a service listener. The listener is not removed if it is not present in the list of listeners.

    </div>

    Parameters:  
    `listener` -

    The service listener to remove.

    </div>

  - <div id="sdk-for-android-navigate-add-com-here-sdk-venue-service-VenueListener" class="section detail">

    ### add

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">add</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-service-venuelistener" title="interface in com.here.sdk.venue.service">VenueListener</a> listener)</span>

    </div>

    <div class="block">

    Adds a venue listener. The listener is not added if it is null or is already present in the list of listeners.

    </div>

    Parameters:  
    `listener` -

    The venue listener to add.

    </div>

  - <div id="sdk-for-android-navigate-remove-com-here-sdk-venue-service-VenueListener" class="section detail">

    ### remove

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">remove</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-service-venuelistener" title="interface in com.here.sdk.venue.service">VenueListener</a> listener)</span>

    </div>

    <div class="block">

    Removes a venue listener. The listener is not removed if it is not present in the list of listeners.

    </div>

    Parameters:  
    `listener` -

    The venue listener to remove.

    </div>

  - <div id="sdk-for-android-navigate-add-com-here-sdk-venue-service-VenueMapListener" class="section detail">

    ### add

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">add</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-service-venuemaplistener" title="interface in com.here.sdk.venue.service">VenueMapListener</a> listener)</span>

    </div>

    <div class="block">

    Adds a venue map listener. The listener is not added if it is null or is already present in the list of listeners.

    </div>

    Parameters:  
    `listener` -

    The venue map listener to add.

    </div>

  - <div id="sdk-for-android-navigate-remove-com-here-sdk-venue-service-VenueMapListener" class="section detail">

    ### remove

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">remove</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-service-venuemaplistener" title="interface in com.here.sdk.venue.service">VenueMapListener</a> listener)</span>

    </div>

    <div class="block">

    Removes a venue map listener. The listener is not removed if it is not present in the list of listeners.

    </div>

    Parameters:  
    `listener` -

    The venue map listener to remove.

    </div>

  - <div id="sdk-for-android-navigate-getInitStatus" class="section detail">

    ### getInitStatus

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-service-venueserviceinitstatus" title="enum class in com.here.sdk.venue.service">VenueServiceInitStatus</a></span> <span class="element-name">getInitStatus</span>()

    </div>

    <div class="block">

    Gets an initialization status.

    </div>

    Returns:  
    The initialization status.

    </div>

  - <div id="sdk-for-android-navigate-isInitialized" class="section detail">

    ### isInitialized

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isInitialized</span>()

    </div>

    <div class="block">

    Checks if the venue service is initialized.

    </div>

    Returns:  
    `True` if the venue service is initialized and `false` otherwise.

    </div>

  - <div id="sdk-for-android-navigate-addVenueToLoad-int" class="section detail">

    ### addVenueToLoad

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addVenueToLoad</span><wbr></wbr><span class="parameters">(int venueId)</span>

    </div>

    <div class="block">

    Adds a venue to the loading queue.

    </div>

    Parameters:  
    `venueId` -

    The id of the venue to load.

    </div>

  - <div id="sdk-for-android-navigate-addVenueToLoad-java-lang-String" class="section detail">

    ### addVenueToLoad

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addVenueToLoad</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> venueIdentifier)</span>

    </div>

    <div class="block">

    Adds a venue to the loading queue.

    </div>

    Parameters:  
    `venueIdentifier` -

    The id of the venue to load.

    </div>

  - <div id="sdk-for-android-navigate-setHrn-java-lang-String" class="section detail">

    ### setHrn

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setHrn</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> hrn)</span>

    </div>

    <div class="block">

    Sets HRN of platform catalog.

    </div>

    Parameters:  
    `hrn` -

    The HRN of platform catalog.

    </div>

  - <div id="sdk-for-android-navigate-setLabeltextPreference-java-util-List" class="section detail">

    ### setLabeltextPreference

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLabeltextPreference</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a>\> labelTextPref)</span>

    </div>

    <div class="block">

    Sets override labelTextPreference for labels.

    </div>

    Parameters:  
    `labelTextPref` -

    The list of string override labelTextPreference. "OCCUPANT_NAMES" - To display only occupant names on map as a label text. Example: Boutique Du Chocolat for id 7348 "SPACE_NAME" - To display only space names on map as a label text. Example: Family Services/First Aid for id 7348 "SPACE_TYPE_NAME" - To display only space types on map as a label text. Example: DEFIBRILLATOR for id 7348 "SPACE_CATEGORY_NAME" - To display only space categories on map as a label text. Example: SAFETY for id 7348 "INTERNAL_ADDRESS" - To display only internal addresses on map as a label text. Example: 51/D for id 7348

    </div>

  - <div id="sdk-for-android-navigate-loadTopologies" class="section detail">

    ### loadTopologies

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">loadTopologies</span>()

    </div>

    <div class="block">

    Lets user load topologies for current session

    </div>

    </div>

  - <div id="sdk-for-android-navigate-loadOptionalFeatures-java-util-List" class="section detail">

    ### loadOptionalFeatures

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">loadOptionalFeatures</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-venue-service-venueservice-venueoptionalfeature" title="enum class in com.here.sdk.venue.service">VenueService.VenueOptionalFeature</a>\> optionalFeatureList)</span>

    </div>

    <div class="block">

    Lets user load optional features for current session.

    </div>

    Parameters:  
    `optionalFeatureList` -

    The list of optional feature enum VenueOptionalFeature.

    </div>

  - <div id="sdk-for-android-navigate-getLanguages" class="section detail">

    ### getLanguages

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a>\></span> <span class="element-name">getLanguages</span>()

    </div>

    <div class="block">

    Gets the languages available in the venue service.

    </div>

    Returns:  
    The languages available in the venue service.

    </div>

  - <div id="sdk-for-android-navigate-getLanguage" class="section detail">

    ### getLanguage

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getLanguage</span>()

    </div>

    <div class="block">

    Gets an active language in the venue service. The venue service will try to load a venue with a translation in the active language. If such translation doesn't exist, a venue will be loaded in its default language.

    </div>

    Returns:  
    The active language.

    </div>

  - <div id="sdk-for-android-navigate-setLanguage-java-lang-String" class="section detail">

    ### setLanguage

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLanguage</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> value)</span>

    </div>

    <div class="block">

    Sets an active language. The venue service will try to load a venue with a translation in the active language. If such translation doesn't exist, a venue will be loaded in its default language.

    </div>

    Parameters:  
    `value` -

    The active language.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

