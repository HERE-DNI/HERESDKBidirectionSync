---
title: "LocationEngine (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-location-locationengine"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-location-package-summary">com.here.sdk.location</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.location.LocationEngine → com.here.sdk.location.LocationEngine

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

All Implemented Interfaces:  
`com.here.sdk.location.AppConfigListener`, <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">`LocationEngineBase`</a>

<div class="type-signature">

<span class="modifiers">public class </span><span class="element-name type-name-label">LocationEngine</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a> implements <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a>, com.here.sdk.location.AppConfigListener</span>

</div>

<div class="block">

This class handles location updates received according to the desired LocationAccuracy or LocationOptions . Each instance of this class will be using internally the same client providing the actual location updates. For that reason, only one LocationEngine can be started at a time. Multiple listeners can be attached, either to receive location updates, see LocationListener , status updates, see LocationStatusListener or location issue has occurred, see LocationIssueListener . When a different LocationAccuracy or LocationOptions is desired, the LocationEngine needs to be stopped and started again.

</div>

</div>

- <div id="sdk-for-android-navigate-constructor-summary" class="section constructor-summary">

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

      LocationEngine ()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Constructor of the LocationEngine

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      LocationEngine ( SDKNativeEngine engine)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Constructor of the LocationEngine

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

      addLocationIssueListener ( LocationIssueListener listener)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Adds a LocationIssueListener to the engine to get notified when a location issue has occurred

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      addLocationListener ( LocationListener listener)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Adds a LocationListener to the engine to get notified when there is a new Location .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      addLocationStatusListener ( LocationStatusListener listener)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Adds a LocationStatusListener to the engine to get notified when there is an important status change.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-location-confirmationstatus" title="enum class in com.here.sdk.location">`ConfirmationStatus`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      confirmHEREPrivacyNoticeException ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  By calling this method, the application developer confirms that they have received an exceptional permission from HERE in written form to \*\*not\*\* include a reference to the HERE Privacy Notice.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-location-confirmationstatus" title="enum class in com.here.sdk.location">`ConfirmationStatus`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      confirmHEREPrivacyNoticeInclusion ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  It is the responsibility of the application developer to ensure that the application user is informed about the collection of characteristic information regarding nearby mobile and Wi-Fi network signals.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      disableVehicleSensors ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Disables access to vehicle's sensor information.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      enableVehicleSensors (androidx.car.app.hardware.CarHardwareManager manager)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  This feature enables the utilization of the vehicle's GNSS and movement sensor information.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-location" title="class in com.here.sdk.core">`Location`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getLastKnownLocation ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the last known location obtained by the engine.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      isStarted ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Checks if the engine is in started state.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      removeLocationIssueListener ( LocationIssueListener listener)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Removes a LocationIssueListener from the engine

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      removeLocationListener ( LocationListener listener)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Removes a LocationListener from the engine

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      removeLocationStatusListener ( LocationStatusListener listener)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Removes a LocationStatusListener from the engine

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">`LocationEngineStatus`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setLastKnownLocationPersistent (boolean persistent)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Enables or disables saving of last known location so it persists between application sessions.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">`LocationEngineStatus`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      start ( LocationAccuracy locationAccuracy)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Starts the location engine with desired LocationAccuracy .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">`LocationEngineStatus`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      start ( LocationOptions locationOptions)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Starts the location engine with desired LocationOptions .

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

  Stops the location engine.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">`LocationEngineStatus`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      updateLocationAccuracy ( LocationAccuracy locationAccuracy)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Reconfigures the location engine with desired LocationAccuracy.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">`LocationEngineStatus`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      updateLocationOptions ( LocationOptions locationOptions)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Reconfigures the location engine with desired LocationOptions.

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

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init" class="section detail">

    ### LocationEngine

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">LocationEngine</span>() throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Constructor of the LocationEngine

    </div>

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> - if engine was not initialized properly

    </div>

  - <div id="sdk-for-android-navigate-init-com-here-sdk-core-engine-SDKNativeEngine" class="section detail">

    ### LocationEngine

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">LocationEngine</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> engine)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Constructor of the LocationEngine

    </div>

    Parameters:  
    `engine` - of the SDK holding internal services and SDK configuration

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> - if engine was not initialized properly

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-start-com-here-sdk-location-LocationAccuracy" class="section detail">

    ### start

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span class="element-name">start</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-location-locationaccuracy" title="enum class in com.here.sdk.location">LocationAccuracy</a> locationAccuracy)</span>

    </div>

    <div class="block">

    Starts the location engine with desired LocationAccuracy . Make sure to call either confirmHEREPrivacyNoticeInclusion() or confirmHEREPrivacyNoticeException() beforehand.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#start(com.here.sdk.location.LocationAccuracy">`start`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">`LocationEngineBase`</a>

    Parameters:  
    `locationAccuracy` - Desired location accuracy

    Returns:  
    the status of the LocationEngine

    Throws:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" class="external-link" title="class or interface in java.lang"><code>IllegalArgumentException</code></a> - if the argument is null

    </div>

  - <div id="sdk-for-android-navigate-start-com-here-sdk-location-LocationOptions" class="section detail">

    ### start

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span class="element-name">start</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-location-locationoptions" title="class in com.here.sdk.location">LocationOptions</a> locationOptions)</span>

    </div>

    <div class="block">

    Starts the location engine with desired LocationOptions . Make sure to call either confirmHEREPrivacyNoticeInclusion() or confirmHEREPrivacyNoticeException() beforehand.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#start(com.here.sdk.location.LocationOptions">`start`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">`LocationEngineBase`</a>

    Parameters:  
    `locationOptions` - Desired location options.

    Returns:  
    the status of the LocationEngine

    Throws:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" class="external-link" title="class or interface in java.lang"><code>IllegalArgumentException</code></a> - if the argument is null

    </div>

  - <div id="sdk-for-android-navigate-updateLocationAccuracy-com-here-sdk-location-LocationAccuracy" class="section detail">

    ### updateLocationAccuracy

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span class="element-name">updateLocationAccuracy</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-location-locationaccuracy" title="enum class in com.here.sdk.location">LocationAccuracy</a> locationAccuracy)</span>

    </div>

    <div class="block">

    Reconfigures the location engine with desired LocationAccuracy. This method is a faster way to change location accuracy for already started location engine, than calling LocationEngineBase.stop() and LocationEngineBase.start(LocationOptions) in sequence. Returns LocationEngineStatus.NOT_READY , if called for unstarted location engine.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#updateLocationAccuracy(com.here.sdk.location.LocationAccuracy">`updateLocationAccuracy`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">`LocationEngineBase`</a>

    Parameters:  
    `locationAccuracy` -

    Desired location accuracy. Requested accuracy is not guaranteed.

    Returns:  
    Engine status. Valid values are defined in <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">`LocationEngineStatus`</a>

    Throws:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" class="external-link" title="class or interface in java.lang"><code>IllegalArgumentException</code></a> - if the argument is null

    </div>

  - <div id="sdk-for-android-navigate-updateLocationOptions-com-here-sdk-location-LocationOptions" class="section detail">

    ### updateLocationOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span class="element-name">updateLocationOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-location-locationoptions" title="class in com.here.sdk.location">LocationOptions</a> locationOptions)</span>

    </div>

    <div class="block">

    Reconfigures the location engine with desired LocationOptions. This method is a faster way to change location options for already started location engine, than calling LocationEngineBase.stop() and LocationEngineBase.start(LocationOptions) in sequence. Returns LocationEngineStatus.NOT_READY , if called for unstarted location engine.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#updateLocationOptions(com.here.sdk.location.LocationOptions">`updateLocationOptions`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">`LocationEngineBase`</a>

    Parameters:  
    `locationOptions` -

    Desired location options.

    Returns:  
    Engine status. Valid values are defined in <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">`LocationEngineStatus`</a>

    Throws:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" class="external-link" title="class or interface in java.lang"><code>IllegalArgumentException</code></a> - if the argument is null

    </div>

  - <div id="sdk-for-android-navigate-stop" class="section detail">

    ### stop

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">stop</span>()

    </div>

    <div class="block">

    Stops the location engine.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#stop(">`stop`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">`LocationEngineBase`</a>

    </div>

  - <div id="sdk-for-android-navigate-isStarted" class="section detail">

    ### isStarted

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isStarted</span>()

    </div>

    <div class="block">

    Checks if the engine is in started state.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#isStarted(">`isStarted`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">`LocationEngineBase`</a>

    Returns:  
    true if started, false otherwise

    </div>

  - <div id="sdk-for-android-navigate-confirmHEREPrivacyNoticeInclusion" class="section detail">

    ### confirmHEREPrivacyNoticeInclusion

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-confirmationstatus" title="enum class in com.here.sdk.location">ConfirmationStatus</a></span> <span class="element-name">confirmHEREPrivacyNoticeInclusion</span>()

    </div>

    <div class="block">

    It is the responsibility of the application developer to ensure that the application user is informed about the collection of characteristic information regarding nearby mobile and Wi-Fi network signals. Additionally, a link to the related HERE Privacy Notice must be made available to the user. This information can be included in the application's Terms & Conditions, Privacy Policy, or otherwise made accessible to the user. An example text for informing users about the data collection: "This application uses location services provided by HERE Technologies. To maintain, improve, and provide these services, HERE Technologies occasionally collects characteristic information about nearby mobile and Wi-Fi network signals. For more information, please refer to the HERE Privacy Notice at: https://legal.here.com/here-network-positioning-via-sdk" By calling this method, the application developer confirms that this information is made available to the end user. For example, it is sufficient to inform users once that using the app requires acceptance of its terms (if any). Then, in the terms include the above mentioned data collection information and a link to the related HERE Privacy Notice. The user is not required to open the terms to acknowledge the data collection details. The "Positioning" example app on GitHub provides an example of this. When the above criteria are met, it is recommended to silently execute this method each time before starting the LocationEngine , as failure to do so will result in the engine being non-functional.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#confirmHEREPrivacyNoticeInclusion(">`confirmHEREPrivacyNoticeInclusion`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">`LocationEngineBase`</a>

    Returns:  
    Immediately returns with <a href="sdk-for-android-navigate-com-here-sdk-location-confirmationstatus#OK">`ConfirmationStatus.OK`</a>.

    </div>

  - <div id="sdk-for-android-navigate-confirmHEREPrivacyNoticeException" class="section detail">

    ### confirmHEREPrivacyNoticeException

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-confirmationstatus" title="enum class in com.here.sdk.location">ConfirmationStatus</a></span> <span class="element-name">confirmHEREPrivacyNoticeException</span>()

    </div>

    <div class="block">

    By calling this method, the application developer confirms that they have received an exceptional permission from HERE in written form to \*\*not\*\* include a reference to the HERE Privacy Notice. As a result, the LocationEngine will not collect characteristic information about the nearby mobile and Wi-Fi network signals. However, the engine will still be fully functional and it will deliver location updates when the exception can be confirmed. Note that this call should not involve user interaction and it should be executed silently by the application before starting the LocationEngine . The permission for exceptional use will be verified asynchronously using your HERE SDK credentials. A missing permission will lead to stopping of the LocationEngine and LocationEngineStatus.PRIVACY_NOTICE_UNCONFIRMED is delivered to LocationStatusListener .

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#confirmHEREPrivacyNoticeException(">`confirmHEREPrivacyNoticeException`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">`LocationEngineBase`</a>

    Returns:  
    Confirmation action status. Valid values are defined in <a href="sdk-for-android-navigate-com-here-sdk-location-confirmationstatus" title="enum class in com.here.sdk.location">`ConfirmationStatus`</a>. A first-time call may result in <a href="sdk-for-android-navigate-com-here-sdk-location-confirmationstatus#PENDING">`ConfirmationStatus.PENDING`</a>, make sure to use the `LocationStatusListener` to get notified on an unconfirmed permission.

    </div>

  - <div id="sdk-for-android-navigate-enableVehicleSensors-androidx-car-app-hardware-CarHardwareManager" class="section detail">

    ### enableVehicleSensors

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">enableVehicleSensors</span><wbr></wbr><span class="parameters">(@NonNull androidx.car.app.hardware.CarHardwareManager manager)</span>

    </div>

    <div class="block">

    This feature enables the utilization of the vehicle's GNSS and movement sensor information. It is recommended to always enable this feature by default when the application supports Android Auto. This allows the phone's positioning sensor information to be augmented with the vehicle's sensor data, resulting in the best possible positioning estimates. However, given the varying quality of car sensor implementations, it is also advisable to provide application users with the option to disable the usage of vehicle sensor information - this would be helpful in case the vehicle reports information that is clearly misleading or contradictory. Furthermore, users should be able to re-enable this feature if the vehicle's capability improves.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#enableVehicleSensors(androidx.car.app.hardware.CarHardwareManager">`enableVehicleSensors`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">`LocationEngineBase`</a>

    Parameters:  
    `manager` - Android Auto car hardware manager.

    </div>

  - <div id="sdk-for-android-navigate-disableVehicleSensors" class="section detail">

    ### disableVehicleSensors

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">disableVehicleSensors</span>()

    </div>

    <div class="block">

    Disables access to vehicle's sensor information.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#disableVehicleSensors(">`disableVehicleSensors`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">`LocationEngineBase`</a>

    </div>

  - <div id="sdk-for-android-navigate-getLastKnownLocation" class="section detail">

    ### getLastKnownLocation

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-location" title="class in com.here.sdk.core">Location</a></span> <span class="element-name">getLastKnownLocation</span>()

    </div>

    <div class="block">

    Gets the last known location obtained by the engine.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#getLastKnownLocation(">`getLastKnownLocation`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">`LocationEngineBase`</a>

    Returns:  
    last known <a href="sdk-for-android-navigate-com-here-sdk-core-location" title="class in com.here.sdk.core">`Location`</a> if available, null if never obtained.

    </div>

  - <div id="sdk-for-android-navigate-addLocationListener-com-here-sdk-core-LocationListener" class="section detail">

    ### addLocationListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addLocationListener</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener" title="interface in com.here.sdk.core">LocationListener</a> listener)</span>

    </div>

    <div class="block">

    Adds a LocationListener to the engine to get notified when there is a new Location .

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#addLocationListener(com.here.sdk.core.LocationListener">`addLocationListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">`LocationEngineBase`</a>

    Parameters:  
    `listener` - The listener to be added

    Throws:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" class="external-link" title="class or interface in java.lang"><code>IllegalArgumentException</code></a> - if the listener is null

    </div>

  - <div id="sdk-for-android-navigate-removeLocationListener-com-here-sdk-core-LocationListener" class="section detail">

    ### removeLocationListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeLocationListener</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener" title="interface in com.here.sdk.core">LocationListener</a> listener)</span>

    </div>

    <div class="block">

    Removes a LocationListener from the engine

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#removeLocationListener(com.here.sdk.core.LocationListener">`removeLocationListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">`LocationEngineBase`</a>

    Parameters:  
    `listener` - The listener to be removed

    Throws:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" class="external-link" title="class or interface in java.lang"><code>IllegalArgumentException</code></a> - if the listener is null

    </div>

  - <div id="sdk-for-android-navigate-addLocationStatusListener-com-here-sdk-location-LocationStatusListener" class="section detail">

    ### addLocationStatusListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addLocationStatusListener</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-location-locationstatuslistener" title="interface in com.here.sdk.location">LocationStatusListener</a> listener)</span>

    </div>

    <div class="block">

    Adds a LocationStatusListener to the engine to get notified when there is an important status change.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#addLocationStatusListener(com.here.sdk.location.LocationStatusListener">`addLocationStatusListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">`LocationEngineBase`</a>

    Parameters:  
    `listener` - The listener to be added

    Throws:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" class="external-link" title="class or interface in java.lang"><code>IllegalArgumentException</code></a> - if the listener is null

    </div>

  - <div id="sdk-for-android-navigate-removeLocationStatusListener-com-here-sdk-location-LocationStatusListener" class="section detail">

    ### removeLocationStatusListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeLocationStatusListener</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-location-locationstatuslistener" title="interface in com.here.sdk.location">LocationStatusListener</a> listener)</span>

    </div>

    <div class="block">

    Removes a LocationStatusListener from the engine

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#removeLocationStatusListener(com.here.sdk.location.LocationStatusListener">`removeLocationStatusListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">`LocationEngineBase`</a>

    Parameters:  
    `listener` - The listener to be removed

    Throws:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" class="external-link" title="class or interface in java.lang"><code>IllegalArgumentException</code></a> - if the listener is null

    </div>

  - <div id="sdk-for-android-navigate-addLocationIssueListener-com-here-sdk-location-LocationIssueListener" class="section detail">

    ### addLocationIssueListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addLocationIssueListener</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-location-locationissuelistener" title="interface in com.here.sdk.location">LocationIssueListener</a> listener)</span>

    </div>

    <div class="block">

    Adds a LocationIssueListener to the engine to get notified when a location issue has occurred

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#addLocationIssueListener(com.here.sdk.location.LocationIssueListener">`addLocationIssueListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">`LocationEngineBase`</a>

    Parameters:  
    `listener` - The listener to be added

    Throws:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" class="external-link" title="class or interface in java.lang"><code>IllegalArgumentException</code></a> - if the listener is null

    </div>

  - <div id="sdk-for-android-navigate-removeLocationIssueListener-com-here-sdk-location-LocationIssueListener" class="section detail">

    ### removeLocationIssueListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeLocationIssueListener</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-location-locationissuelistener" title="interface in com.here.sdk.location">LocationIssueListener</a> listener)</span>

    </div>

    <div class="block">

    Removes a LocationIssueListener from the engine

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#removeLocationIssueListener(com.here.sdk.location.LocationIssueListener">`removeLocationIssueListener`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">`LocationEngineBase`</a>

    Parameters:  
    `listener` - The listener to be removed

    Throws:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" class="external-link" title="class or interface in java.lang"><code>IllegalArgumentException</code></a> - if the listener is null

    </div>

  - <div id="sdk-for-android-navigate-setLastKnownLocationPersistent-boolean" class="section detail">

    ### setLastKnownLocationPersistent

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span class="element-name">setLastKnownLocationPersistent</span><wbr></wbr><span class="parameters">(boolean persistent)</span>

    </div>

    <div class="block">

    Enables or disables saving of last known location so it persists between application sessions. Defaults to enabled.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase#setLastKnownLocationPersistent(boolean">`setLastKnownLocationPersistent`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginebase" title="interface in com.here.sdk.location">`LocationEngineBase`</a>

    Parameters:  
    `persistent` - If true enables last known location to be saved persistently, or if false disables it.

    Returns:  
    LocationEngineStatus.OK always.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

