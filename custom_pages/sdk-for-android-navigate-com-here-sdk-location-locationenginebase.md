---
title: "LocationEngineBase (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-location-locationenginebase"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-location-package-summary">com.here.sdk.location</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

All Known Implementing Classes:  
<a href="sdk-for-android-navigate-com-here-sdk-location-locationengine" title="class in com.here.sdk.location">`LocationEngine`</a>

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">LocationEngineBase</span>

</div>

<div class="block">

Public interface that describes the behaviour of LocationEngine . Implementation is platform-specific.

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      addLocationIssueListener ( LocationIssueListener listener)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Adds a LocationIssueListener to the engine to get notified when a location issue has occurred.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      addLocationListener ( LocationListener listener)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Adds a LocationListener to the engine to get notified when there is a new location update available.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      addLocationStatusListener ( LocationStatusListener listener)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Adds a LocationStatusListener to the engine to get notified when there is an important status change.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-location-confirmationstatus" title="enum class in com.here.sdk.location">`ConfirmationStatus`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      confirmHEREPrivacyNoticeException ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  By calling this method, the application developer confirms that they have received an exceptional permission from HERE in written form to not include a reference to the HERE Privacy Notice.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-location-confirmationstatus" title="enum class in com.here.sdk.location">`ConfirmationStatus`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      confirmHEREPrivacyNoticeInclusion ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  It is the responsibility of the application developer to ensure that the application user is informed about the collection of characteristic information regarding nearby mobile and Wi-Fi network signals.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      disableVehicleSensors ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Disables access to vehicle's sensor information.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      enableVehicleSensors (androidx.car.app.hardware.CarHardwareManager manager)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  This feature enables the utilization of the vehicle's GNSS and movement sensor information.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-core-location" title="class in com.here.sdk.core">`Location`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getLastKnownLocation ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the last known location obtained by the LocationEngine .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      isStarted ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Checks if the engine is in started state.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      removeLocationIssueListener ( LocationIssueListener listener)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Removes a LocationIssueListener from the engine.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      removeLocationListener ( LocationListener listener)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Removes a LocationListener from the engine.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      removeLocationStatusListener ( LocationStatusListener listener)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Removes a LocationStatusListener from the engine.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">`LocationEngineStatus`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setLastKnownLocationPersistent (boolean persistent)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Enables or disables saving of last known location so that it persists between application sessions.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">`LocationEngineStatus`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      start ( LocationAccuracy locationAccuracy)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Starts the location engine with desired LocationAccuracy .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">`LocationEngineStatus`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      start ( LocationOptions locationOptions)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Starts the location engine with desired LocationOptions .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      stop ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Stops the location engine.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">`LocationEngineStatus`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      updateLocationAccuracy ( LocationAccuracy locationAccuracy)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Reconfigures the location engine with desired LocationAccuracy .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">`LocationEngineStatus`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      updateLocationOptions ( LocationOptions locationOptions)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Reconfigures the location engine with desired LocationOptions .

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-start-com-here-sdk-location-LocationAccuracy" class="section detail">

    ### start

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span class="element-name">start</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-location-locationaccuracy" title="enum class in com.here.sdk.location">LocationAccuracy</a> locationAccuracy)</span>

    </div>

    <div class="block">

    Starts the location engine with desired LocationAccuracy . Returns LocationEngineStatus.ALREADY_STARTED , if start(LocationOptions) is called again without stop() in between. Make sure to call either confirmHEREPrivacyNoticeInclusion() or confirmHEREPrivacyNoticeException() beforehand.

    </div>

    Parameters:  
    `locationAccuracy` -

    Desired location accuracy. Requested accuracy is not guaranteed.

    Returns:  
    Engine status. Valid values are defined in <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">`LocationEngineStatus`</a>

    </div>

  - <div id="sdk-for-android-navigate-start-com-here-sdk-location-LocationOptions" class="section detail">

    ### start

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span class="element-name">start</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-location-locationoptions" title="class in com.here.sdk.location">LocationOptions</a> locationOptions)</span>

    </div>

    <div class="block">

    Starts the location engine with desired LocationOptions . Returns LocationEngineStatus.ALREADY_STARTED , if start(LocationOptions) is called again without stop() in between. Make sure to call either confirmHEREPrivacyNoticeInclusion() or confirmHEREPrivacyNoticeException() beforehand.

    </div>

    Parameters:  
    `locationOptions` -

    Desired location options.

    Returns:  
    Engine status. Valid values are defined in <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">`LocationEngineStatus`</a>

    </div>

  - <div id="sdk-for-android-navigate-updateLocationAccuracy-com-here-sdk-location-LocationAccuracy" class="section detail">

    ### updateLocationAccuracy

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span class="element-name">updateLocationAccuracy</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-location-locationaccuracy" title="enum class in com.here.sdk.location">LocationAccuracy</a> locationAccuracy)</span>

    </div>

    <div class="block">

    Reconfigures the location engine with desired LocationAccuracy . This method is a faster way to change location accuracy for already started location engine, than calling stop() and start(LocationOptions) in sequence. Returns LocationEngineStatus.NOT_READY , if called for unstarted location engine.

    </div>

    Parameters:  
    `locationAccuracy` -

    Desired location accuracy. Requested accuracy is not guaranteed.

    Returns:  
    Engine status. Valid values are defined in <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">`LocationEngineStatus`</a>

    </div>

  - <div id="sdk-for-android-navigate-updateLocationOptions-com-here-sdk-location-LocationOptions" class="section detail">

    ### updateLocationOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span class="element-name">updateLocationOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-location-locationoptions" title="class in com.here.sdk.location">LocationOptions</a> locationOptions)</span>

    </div>

    <div class="block">

    Reconfigures the location engine with desired LocationOptions . This method is a faster way to change location options for already started location engine, than calling stop() and start(LocationOptions) in sequence. Returns LocationEngineStatus.NOT_READY , if called for unstarted location engine.

    </div>

    Parameters:  
    `locationOptions` -

    Desired location options.

    Returns:  
    Engine status. Valid values are defined in <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">`LocationEngineStatus`</a>

    </div>

  - <div id="sdk-for-android-navigate-stop" class="section detail">

    ### stop

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">stop</span>()

    </div>

    <div class="block">

    Stops the location engine.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-confirmHEREPrivacyNoticeInclusion" class="section detail">

    ### confirmHEREPrivacyNoticeInclusion

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-confirmationstatus" title="enum class in com.here.sdk.location">ConfirmationStatus</a></span> <span class="element-name">confirmHEREPrivacyNoticeInclusion</span>()

    </div>

    <div class="block">

    It is the responsibility of the application developer to ensure that the application user is informed about the collection of characteristic information regarding nearby mobile and Wi-Fi network signals. Additionally, a link to the related HERE Privacy Notice must be made available to the user. This information can be included in the application's Terms & Conditions, Privacy Policy, or otherwise made accessible to the user. An example text for informing users about the data collection: "This application uses location services provided by HERE Technologies. To maintain, improve, and provide these services, HERE Technologies occasionally collects characteristic information about nearby mobile and Wi-Fi network signals. For more information, please refer to the HERE Privacy Notice at: https://legal.here.com/en-gb/here-network-positioning-via-sdk" Note: By calling this method, the application developer confirms that this information is made available to the end user. For example, it is sufficient to inform users once that using the app requires acceptance of its terms (if any). Then, in the terms include the above mentioned data collection information and a link to the related HERE Privacy Notice. The user is not required to open the terms to acknowledge the data collection details. The "Positioning" example app on GitHub provides an example of this. When the above criteria are met, it is recommended to silently execute this method each time before starting the LocationEngine , as failure to do so will result in the engine being non-functional.

    </div>

    Returns:  
    Immediately returns with <a href="sdk-for-android-navigate-com-here-sdk-location-confirmationstatus#OK">`ConfirmationStatus.OK`</a>.

    </div>

  - <div id="sdk-for-android-navigate-confirmHEREPrivacyNoticeException" class="section detail">

    ### confirmHEREPrivacyNoticeException

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-confirmationstatus" title="enum class in com.here.sdk.location">ConfirmationStatus</a></span> <span class="element-name">confirmHEREPrivacyNoticeException</span>()

    </div>

    <div class="block">

    By calling this method, the application developer confirms that they have received an exceptional permission from HERE in written form to not include a reference to the HERE Privacy Notice. As a result, the LocationEngine will not collect characteristic information about the nearby mobile and Wi-Fi network signals. However, the engine will still be fully functional and it will deliver location updates when the exception can be confirmed. Note that this call should not involve user interaction and it should be executed silently by the application before starting the LocationEngine . The permission for exceptional use will be verified asynchronously using your HERE SDK credentials. A missing permission will lead to stopping of the LocationEngine and LocationEngineStatus.PRIVACY_NOTICE_UNCONFIRMED is delivered to LocationStatusListener .

    </div>

    Returns:  
    Confirmation action status. Valid values are defined in <a href="sdk-for-android-navigate-com-here-sdk-location-confirmationstatus" title="enum class in com.here.sdk.location">`ConfirmationStatus`</a>. A first-time call may result in <a href="sdk-for-android-navigate-com-here-sdk-location-confirmationstatus#PENDING">`ConfirmationStatus.PENDING`</a>, make sure to use the `LocationStatusListener` to get notified on an unconfirmed permission.

    </div>

  - <div id="sdk-for-android-navigate-addLocationListener-com-here-sdk-core-LocationListener" class="section detail">

    ### addLocationListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">addLocationListener</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener" title="interface in com.here.sdk.core">LocationListener</a> listener)</span>

    </div>

    <div class="block">

    Adds a LocationListener to the engine to get notified when there is a new location update available. Supports more than one listener, instance is added only once.

    </div>

    Parameters:  
    `listener` -

    The listener.

    </div>

  - <div id="sdk-for-android-navigate-removeLocationListener-com-here-sdk-core-LocationListener" class="section detail">

    ### removeLocationListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">removeLocationListener</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener" title="interface in com.here.sdk.core">LocationListener</a> listener)</span>

    </div>

    <div class="block">

    Removes a LocationListener from the engine.

    </div>

    Parameters:  
    `listener` -

    The listener.

    </div>

  - <div id="sdk-for-android-navigate-addLocationStatusListener-com-here-sdk-location-LocationStatusListener" class="section detail">

    ### addLocationStatusListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">addLocationStatusListener</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-location-locationstatuslistener" title="interface in com.here.sdk.location">LocationStatusListener</a> listener)</span>

    </div>

    <div class="block">

    Adds a LocationStatusListener to the engine to get notified when there is an important status change. Supports more than one listener, instance is added only once.

    </div>

    Parameters:  
    `listener` -

    The listener.

    </div>

  - <div id="sdk-for-android-navigate-removeLocationStatusListener-com-here-sdk-location-LocationStatusListener" class="section detail">

    ### removeLocationStatusListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">removeLocationStatusListener</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-location-locationstatuslistener" title="interface in com.here.sdk.location">LocationStatusListener</a> listener)</span>

    </div>

    <div class="block">

    Removes a LocationStatusListener from the engine.

    </div>

    Parameters:  
    `listener` -

    The listener.

    </div>

  - <div id="sdk-for-android-navigate-addLocationIssueListener-com-here-sdk-location-LocationIssueListener" class="section detail">

    ### addLocationIssueListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">addLocationIssueListener</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-location-locationissuelistener" title="interface in com.here.sdk.location">LocationIssueListener</a> listener)</span>

    </div>

    <div class="block">

    Adds a LocationIssueListener to the engine to get notified when a location issue has occurred. Supports more than one listener, instance is added only once.

    </div>

    Parameters:  
    `listener` -

    The listener.

    </div>

  - <div id="sdk-for-android-navigate-removeLocationIssueListener-com-here-sdk-location-LocationIssueListener" class="section detail">

    ### removeLocationIssueListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">removeLocationIssueListener</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-location-locationissuelistener" title="interface in com.here.sdk.location">LocationIssueListener</a> listener)</span>

    </div>

    <div class="block">

    Removes a LocationIssueListener from the engine.

    </div>

    Parameters:  
    `listener` -

    The listener.

    </div>

  - <div id="sdk-for-android-navigate-setLastKnownLocationPersistent-boolean" class="section detail">

    ### setLastKnownLocationPersistent

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span class="element-name">setLastKnownLocationPersistent</span><wbr></wbr><span class="parameters">(boolean persistent)</span>

    </div>

    <div class="block">

    Enables or disables saving of last known location so that it persists between application sessions. Defaults to enabled.

    </div>

    Parameters:  
    `persistent` -

    Set to `true` to enable last known location to be saved persistently, or `false` to disable it.

    Returns:  
    <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus#OK">`LocationEngineStatus.OK`</a> if call succeeds. <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus#NOT_SUPPORTED">`LocationEngineStatus.NOT_SUPPORTED`</a> on platforms which do not support controlling of last known location saving.

    </div>

  - <div id="sdk-for-android-navigate-enableVehicleSensors-androidx-car-app-hardware-CarHardwareManager" class="section detail">

    ### enableVehicleSensors

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">enableVehicleSensors</span><wbr></wbr><span class="parameters">(@NonNull androidx.car.app.hardware.CarHardwareManager manager)</span>

    </div>

    <div class="block">

    This feature enables the utilization of the vehicle's GNSS and movement sensor information. It is recommended to always enable this feature by default when the application supports Android Auto. This allows the phone's positioning sensor information to be augmented with the vehicle's sensor data, resulting in the best possible positioning estimates. However, given the varying quality of car sensor implementations, it is also advisable to provide application users with the option to disable the usage of vehicle sensor information - this would be helpful in case the vehicle reports information that is clearly misleading or contradictory. Furthermore, users should be able to re-enable this feature if the vehicle's capability improves.

    </div>

    Parameters:  
    `manager` -

    Android Auto car hardware manager.

    </div>

  - <div id="sdk-for-android-navigate-disableVehicleSensors" class="section detail">

    ### disableVehicleSensors

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">disableVehicleSensors</span>()

    </div>

    <div class="block">

    Disables access to vehicle's sensor information.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-getLastKnownLocation" class="section detail">

    ### getLastKnownLocation

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-location" title="class in com.here.sdk.core">Location</a></span> <span class="element-name">getLastKnownLocation</span>()

    </div>

    <div class="block">

    Gets the last known location obtained by the LocationEngine . It is persisted throughout the app's lifecycle. This property can be obtained without starting the LocationEngine . However, the initial value might be null if no location has ever been obtained by the LocationEngine . The time attribute of the Location object indicates when the last location was obtained. Note: In order to receive continuous location updates, add a LocationListener .

    </div>

    Returns:  
    The last known location obtained by the `LocationEngine`. It is persisted throughout the app's lifecycle.

    </div>

  - <div id="sdk-for-android-navigate-isStarted" class="section detail">

    ### isStarted

    <div class="member-signature">

    <span class="return-type">boolean</span> <span class="element-name">isStarted</span>()

    </div>

    <div class="block">

    Checks if the engine is in started state.

    </div>

    Returns:  
    Checks if the engine is in started state.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

