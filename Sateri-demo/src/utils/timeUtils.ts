import { ref, onMounted, onUnmounted } from 'vue';
import { format } from 'date-fns';

export function useCurrentTime() {
  const currentTime = ref('');
  const timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;

  const updateTime = () => {
    const now = new Date();
    const formattedDate = format(now, 'yyyy-MM-dd HH:mm');
    currentTime.value = `${formattedDate}`;
  };

  onMounted(() => {
    updateTime();
    const interval = setInterval(updateTime, 60000); // 每分钟更新一次
    onUnmounted(() => {
      clearInterval(interval);
    });
  });

  return {
    currentTime,
    timezone
  };
}