if [ ""$(echo $(nmcli radio wifi)
) = 'enabled' ]; then
    nmcli radio wifi off
else
    nmcli radio wifi on
fi
