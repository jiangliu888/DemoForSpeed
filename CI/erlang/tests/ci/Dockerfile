FROM airwalk/ubuntu:16.04

COPY ./aiwan-uranus*.deb /root
WORKDIR /root
RUN sudo dpkg -i aiwan-uranus*.deb
RUN echo '#!/bin/bash' >> run; \
    echo 'set -x' >> run; \
    echo '/usr/local/bin/aiwan-uranus restart' >> run; \
    echo 'sleep 60' >> run; \
    echo 'echo "list" | /opt/aiwan/uranus/apache-karaf-3.0.8/bin/client > bundle' >> run; \
    echo 'ret=`grep "Active" bundle | grep "gaea\|cronus\|thea" |wc -l`' >> run; \
    echo '[ $ret -ne 3 ] && /usr/local/bin/aiwan-uranus restart || rm bundle' >> run; \
    echo 'tail -f /dev/null' >> run
RUN chmod u+x run


CMD ["/bin/bash", "-c", "/root/run"]
